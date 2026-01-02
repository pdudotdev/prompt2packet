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

def main():
    print(Style.BRIGHT + "➥ Describe traffic to generate:\n≫ " + Style.RESET_ALL, end="")
    user_input = input()

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
            followup = input()

            try:
                update = interpret_intent(followup)
            except Exception as e:
                print(Fore.RED + Style.BRIGHT + f"AI error: {e}" + Style.RESET_ALL)
                return

            intent_data.update(update)
            continue

        schema = PROTOCOLS[protocol]["schema"]

        try:
            intent = schema.model_validate(intent_data)
        except ValidationError as ve:
            missing = _missing_required_fields(ve)

            # If it's not missing fields, show the real validation error
            if not missing:
                print(Fore.RED + Style.BRIGHT + "Invalid input:" + Style.RESET_ALL)
                for e in ve.errors():
                    print(" -", e.get("loc"), e.get("msg"))
                return

            question = build_clarification_question(protocol=protocol, missing_fields=missing, current_intent=intent_data)
            print(Fore.YELLOW + Style.BRIGHT + question + Style.RESET_ALL)
            print(Style.BRIGHT + "≫ " + Style.RESET_ALL, end="")
            followup = input()

            try:
                update = interpret_intent(followup)
            except Exception as e:
                print(Fore.RED + Style.BRIGHT + f"AI error: {e}" + Style.RESET_ALL)
                return

            intent_data.update(update)
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
    main()
