from config import MAX_PACKETS

def validate_intent(intent):
    if intent.count > MAX_PACKETS * 0.8:
        print("[WARNING] High packet volume requested")
    elif intent.count > MAX_PACKETS:
        raise ValueError("Packet count exceeds allowed limit")
