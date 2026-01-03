# Load API key from .env
from dotenv import load_dotenv
load_dotenv()

from ai.interpreter import interpret_intent, build_clarification_question
from validation.rules import validate_intent
from planner.execution import build_execution_plan
from sender.transmit import send_packets
from observe.explain import explain_results
from pydantic import ValidationError
from registry import PROTOCOLS
from config import REQUIRE_ROOT
from colorama import Fore, Style
from banner import BANNER
import argparse
import sys
import os

# Require root priv
if REQUIRE_ROOT and os.geteuid() != 0:
    raise PermissionError(Fore.RED + Style.BRIGHT + "＄ Root privileges required" + Style.RESET_ALL)

# Test mode: OFF by default
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', required=False, help='Enable test mode')
    return parser.parse_args()

print(BANNER)
args = parse_arguments()
TEST_MODE = args.test
if not TEST_MODE:
    print("\n★ Mode: " + Fore.GREEN + Style.BRIGHT + "LIVE\n" + Style.RESET_ALL)
else:
    print("\n★ Mode: " + Fore.RED + Style.BRIGHT + "TEST\n" + Style.RESET_ALL)

def _missing_required_fields(err: ValidationError) -> list[str]:
    missing = []
    for e in err.errors():
        # Pydantic v2 missing required field
        if e.get("type") == "missing":
            loc = e.get("loc", ())
            if loc:
                # top-level field name
                missing.append(str(loc[0]))
    # unique, stable order
    seen = set()
    out = []
    for m in missing:
        if m not in seen:
            seen.add(m)
            out.append(m)
    return out

def _friendly_validation_error(err: ValidationError) -> str:
    for e in err.errors():
        loc = e.get("loc", ())
        msg = e.get("msg", "").lower()

        field = loc[0] if loc else "value"

        # Range / bounds errors
        if "greater than" in msg or "less than" in msg:
            return (
                f"The value provided for '{field}' is outside the allowed range. "
                "Please provide a valid value."
            )

        # Type errors
        if "type" in msg or "integer" in msg:
            return (
                f"The value provided for '{field}' has the wrong type. "
                "Please provide a valid number."
            )

        # IP / address errors
        if "ip" in msg:
            return (
                f"The value provided for '{field}' is not a valid IPv4 address "
                "or address range."
            )

        # Port errors
        if "port" in field:
            return (
                "Port values must be between 1 and 65535."
            )

    return "Invalid input. Please review the values you provided."

def run_once():
    print(Style.BRIGHT + "➥ Describe traffic to generate (Ctrl+C to exit):\n≫ " + Style.RESET_ALL, end="")
    try:
        user_input = input()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nExiting on user request." + Style.RESET_ALL)
        sys.exit(0)

    # Step 1: best-effort extraction
    try:
        intent_data = interpret_intent(user_input)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"AI error: {e}" + Style.RESET_ALL)
        return

    # Step 2: clarification loop
    while True:
        protocol = intent_data.get("protocol")

        # Protocol missing or unsupported → ask for protocol explicitly
        if protocol not in PROTOCOLS:
            missing = ["protocol"]
            question = build_clarification_question(protocol=None, missing_fields=missing, current_intent=intent_data)
            print(Fore.YELLOW + Style.BRIGHT + question + Style.RESET_ALL)
            print(Style.BRIGHT + "≫ " + Style.RESET_ALL, end="")
            try:
                followup = input()
            except KeyboardInterrupt:
                print(Fore.RED + Style.BRIGHT + "\nExiting on user request." + Style.RESET_ALL)
                sys.exit(0)

            try:
                update = interpret_intent(followup)
            except Exception as e:
                print(Fore.RED + Style.BRIGHT + f"AI error: {e}" + Style.RESET_ALL)
                return

            if protocol:
                update.pop("protocol", None)  # don't allow followups to overwrite protocol
            for k, v in update.items():
                if v is not None:
                    intent_data[k] = v

            continue

        schema = PROTOCOLS[protocol]["schema"]

        # Normalize user-friendly fields → schema fields
        if "interval" in intent_data and "interval_ms" not in intent_data:
            intent_data["interval_ms"] = intent_data.pop("interval")

        try:
            intent = schema.model_validate(intent_data)
        except ValidationError as ve:
            missing = _missing_required_fields(ve)

            if not missing:
                friendly = _friendly_validation_error(ve)
                print(Fore.RED + Style.BRIGHT + friendly + Style.RESET_ALL)
                return

            question = build_clarification_question(protocol=protocol, missing_fields=missing, current_intent=intent_data)
            print(Fore.YELLOW + Style.BRIGHT + question + Style.RESET_ALL)
            print(Style.BRIGHT + "≫ " + Style.RESET_ALL, end="")
            try:
                followup = input()
            except KeyboardInterrupt:
                print(Fore.RED + Style.BRIGHT + "\nExiting on user request." + Style.RESET_ALL)
                sys.exit(0)

            try:
                update = interpret_intent(followup)
            except Exception as e:
                print(Fore.RED + Style.BRIGHT + f"AI error: {e}" + Style.RESET_ALL)
                return

            for k, v in update.items():
                if v is not None:
                    intent_data[k] = v

            continue

        # Additional rules
        try:
            validate_intent(intent)
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + f"Validation error: {e}" + Style.RESET_ALL)
            return

        # Valid? Then execute
        plan = build_execution_plan(intent)

        results = send_packets(plan, test_mode=TEST_MODE)
        if TEST_MODE:
            for pkt in results["packets"]:
                print(pkt.summary())

        explain_results(intent, plan, results)
        return

if __name__ == "__main__":
    while True:
        try:
            run_once()
        except KeyboardInterrupt:
            print(Fore.RED + Style.BRIGHT + "\nExiting. Goodbye." + Style.RESET_ALL)
            sys.exit(0)

        # After one full run finishes
        print()
        try:
            again = input(
                Style.BRIGHT
                + Fore.GREEN
                + "▶ Generate more traffic? (y/n): "
                + Style.RESET_ALL
            ).strip().lower()
        except KeyboardInterrupt:
            print(Fore.RED + Style.BRIGHT + "\nExiting. Goodbye." + Style.RESET_ALL)
            sys.exit(0)

        if again not in ("y", "yes"):
            print(Fore.RED + Style.BRIGHT + "\nSession ended." + Style.RESET_ALL)
            break

