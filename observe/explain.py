def explain_results(intent, results):
    print("\nExecution summary:")
    print(f"- Protocol: {intent.protocol.upper()}")
    print(f"- Packets sent: {results['sent']}")
