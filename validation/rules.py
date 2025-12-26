from config import MAX_PACKETS

def validate_intent(intent):
    if intent.protocol == "tcp":
        if "SYN" in intent.flags and "ACK" in intent.flags:
            if intent.seq is None:
                raise ValueError("TCP SYN+ACK requires sequence number")

    if intent.count > MAX_PACKETS * 0.8:
        print("[WARNING] High packet volume requested")
    elif intent.count > MAX_PACKETS:
        raise ValueError("Packet count exceeds allowed limit")
