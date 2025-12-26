from ai.interpreter import interpret_intent
from validation.rules import validate_intent
from planner.execution import build_execution_plan
from sender.transmit import send_packets
from observe.explain import explain_results
from registry import PROTOCOLS
from config import REQUIRE_ROOT
from dotenv import load_dotenv
import os

# Require root priv
if REQUIRE_ROOT and os.geteuid() != 0:
    raise PermissionError("Root privileges required")

# Load API key from .env
load_dotenv()

def main():
    user_input = input("Describe traffic to generate:\n> ")

    intent_data = interpret_intent(user_input)
    protocol = intent_data.get("protocol")

    if protocol not in PROTOCOLS:
        raise ValueError(f"Unsupported protocol: {protocol}")

    schema = PROTOCOLS[protocol]["schema"]
    intent = schema.model_validate(intent_data)

    validate_intent(intent)

    plan = build_execution_plan(intent)
    results = send_packets(plan)

    explain_results(intent, plan, results)

if __name__ == "__main__":
    main()
