from config import SEND_ENABLED

def explain_results(intent, plan, results):
    print("\nExecution summary:")
    print(f"- Protocol: {intent.protocol.upper()}")
    print(f"- Packets sent: {results['sent']}")
    print(f"- Mode: {'LIVE' if SEND_ENABLED else 'DRY-RUN'}")
