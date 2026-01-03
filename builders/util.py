from ipaddress import IPv4Address
import random


def expand_ip(value, index):
    # Single IP
    if isinstance(value, (str, IPv4Address)):
        return str(value)

    # IP range (dict from model_dump)
    if isinstance(value, dict):
        start = int(IPv4Address(value["start"]))
        end = int(IPv4Address(value["end"]))

    # IP range (object, defensive)
    elif hasattr(value, "start") and hasattr(value, "end"):
        start = int(value.start)
        end = int(value.end)

    else:
        raise TypeError(f"Unsupported IP value: {value}")

    if end < start:
        raise ValueError("IP range end must be >= start")

    span = end - start + 1
    return str(IPv4Address(start + (index % span)))


def expand_port(value, index):
    # Single port
    if isinstance(value, int):
        return value

    # Port range (dict)
    if isinstance(value, dict):
        start = value["start"]
        end = value["end"]

    # Port range (object, defensive)
    elif hasattr(value, "start") and hasattr(value, "end"):
        start = value.start
        end = value.end

    else:
        raise TypeError(f"Unsupported port value: {value}")

    if end < start:
        raise ValueError("Port range end must be >= start")

    span = end - start + 1
    return start + (index % span)


def choose_ephemeral_port():
    return random.randint(32768, 60999)
