# Load API key from .env
from dotenv import load_dotenv
load_dotenv()

from ai.interpreter import interpret_intent, build_clarification_question
from sender.transmit import send_packets
from pydantic import ValidationError
from schemas.tcp import TCPIntent
from schemas.udp import UDPIntent
from config import REQUIRE_ROOT
from colorama import Fore, Style
from docs.banner import BANNER
import argparse
import sys
import os

# Require root priv
if REQUIRE_ROOT and os.geteuid() != 0:
    raise PermissionError(Fore.RED + Style.BRIGHT + "＄ Root privileges required" + Style.RESET_ALL)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Enable test mode')
    return parser.parse_args()

print(BANNER)
args = parse_arguments()
TEST_MODE = args.test

print(
    "\n★ Mode: "
    + (Fore.RED if TEST_MODE else Fore.GREEN)
    + Style.BRIGHT
    + ("TEST\n" if TEST_MODE else "LIVE\n")
    + Style.RESET_ALL
)

def explain_results(intent, results):
    print(Fore.GREEN + Style.BRIGHT + "\nExecution summary:" + Style.RESET_ALL)
    print(f"• Protocol: {intent.protocol.upper()}")
    print(f"• Packets sent: {results['sent']}")

def _missing_required_fields(err: ValidationError) -> list[str]:
    missing = []
    for e in err.errors():
        if e.get("type") == "missing":
            loc = e.get("loc", ())
            if loc:
                missing.append(str(loc[0]))

    # dedupe, preserve order
    seen = set()
    out = []
    for m in missing:
        if m not in seen:
            seen.add(m)
            out.append(m)
    return out

def _invalid_fields(err: ValidationError) -> list[str]:
    invalid = []
    for e in err.errors():
        if e.get("type") != "missing":
            loc = e.get("loc", ())
            if loc:
                invalid.append(str(loc[0]))

    # dedupe
    seen = set()
    out = []
    for f in invalid:
        if f not in seen:
            seen.add(f)
            out.append(f)
    return out

def main():
    print(Style.BRIGHT + "➥ Describe traffic to generate (Ctrl+C to exit):\n≫ " + Style.RESET_ALL, end="")
    try:
        user_input = input()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nExiting on user request." + Style.RESET_ALL)
        sys.exit(0)

    # Step 1: AI extraction
    try:
        intent_data = interpret_intent(user_input)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"AI error: {e}" + Style.RESET_ALL)
        return

    # Step 2: clarification + validation loop
    while True:
        protocol = intent_data.get("protocol")

        # Missing protocol → ask explicitly
        if protocol not in ("tcp", "udp"):
            question = build_clarification_question(
                protocol=None,
                missing_fields=["protocol"],
                current_intent=intent_data,
            )
            print(Fore.YELLOW + Style.BRIGHT + question + Style.RESET_ALL)
            print(Style.BRIGHT + "≫ " + Style.RESET_ALL, end="")

            try:
                followup = input()
            except KeyboardInterrupt:
                print(Fore.RED + Style.BRIGHT + "\nExiting on user request." + Style.RESET_ALL)
                sys.exit(0)

            update = interpret_intent(followup)
            intent_data.update({k: v for k, v in update.items() if v is not None})
            continue

        # Pick schema explicitly
        schema_cls = TCPIntent if protocol == "tcp" else UDPIntent

        # Normalize user-friendly aliases
        if "interval" in intent_data and "interval_ms" not in intent_data:
            intent_data["interval_ms"] = intent_data.pop("interval")

        # Normalize TCP flags if AI returned a single string
        if protocol == "tcp":
            flags = intent_data.get("flags")
            if isinstance(flags, str):
                intent_data["flags"] = [flags.upper()]

        try:
            intent = schema_cls.model_validate(intent_data)
        except ValidationError as ve:
            missing = _missing_required_fields(ve)
            invalid = _invalid_fields(ve)

            # Invalid values lead to HARD ERROR
            if invalid:
                print(Fore.RED + Style.BRIGHT + f"Invalid value for field(s): {', '.join(invalid)}" + Style.RESET_ALL)
                return

            # Missing fields lead to clarification
            if missing:
                question = build_clarification_question(
                    protocol=protocol,
                    missing_fields=missing,
                    current_intent=intent_data,
                )
            print(Fore.YELLOW + Style.BRIGHT + question + Style.RESET_ALL)
            print(Style.BRIGHT + "≫ " + Style.RESET_ALL, end="")

            try:
                followup = input()
            except KeyboardInterrupt:
                print(Fore.RED + Style.BRIGHT + "\nExiting on user request." + Style.RESET_ALL)
                sys.exit(0)

            update = interpret_intent(followup)
            intent_data.update({k: v for k, v in update.items() if v is not None})
            continue

        # Step 3: execute
        intent_dict = intent.model_dump()
        results = send_packets(intent_dict, test_mode=TEST_MODE)

        if TEST_MODE:
            for pkt in results["packets"]:
                print(pkt.summary())

        explain_results(intent, results)
        return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nExiting. Goodbye." + Style.RESET_ALL)
        sys.exit(0)
