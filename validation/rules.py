from config import MAX_PACKETS

def validate_intent(intent):
    # Packet count validation
    if intent.count > MAX_PACKETS * 0.8:
        print("[WARNING] High packet volume requested")
    elif intent.count > MAX_PACKETS:
        raise ValueError("Packet count exceeds allowed limit")

    # TCP-specific validation
    if intent.protocol == "tcp":
        if intent.window is not None and not (0 <= intent.window <= 65535):
            raise ValueError("TCP window must be between 0 and 65535")

        if intent.seq is not None and not (0 <= intent.seq <= 0xFFFFFFFF):
            raise ValueError("TCP sequence number must be 0–4294967295")

        if intent.ttl is not None and not (0 <= intent.ttl <= 255):
            raise ValueError("IP TTL must be between 0 and 255")