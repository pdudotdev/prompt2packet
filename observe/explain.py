def explain_results(intent, plan, results):
    print("\nExecution summary:")
    print(f"- Protocol: {intent.protocol.upper()}")
    print(f"- Packets sent: {results['sent']}")
