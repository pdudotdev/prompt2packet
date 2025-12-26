from ipaddress import IPv4Address
import random

def expand_ip(value, index):
    # Single IP (string or IPv4Address)
    if isinstance(value, (str, IPv4Address)):
        return str(value)

    # IP range dict: {"start": "...", "end": "..."}
    if isinstance(value, dict):
        start = int(IPv4Address(value["start"]))
        end = int(IPv4Address(value["end"]))
        return str(IPv4Address(start + (index % (end - start + 1))))

    raise TypeError(f"Unsupported IP value: {value}")

def expand_port(value, index):
    # Single port
    if isinstance(value, int):
        return value

    # Port range dict
    if isinstance(value, dict):
        start = value["start"]
        end = value["end"]
        return start + (index % (end - start + 1))

    raise TypeError(f"Unsupported port value: {value}")

def choose_ephemeral_port():
    return random.randint(32768, 60999)