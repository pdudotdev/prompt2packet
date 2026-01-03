from builders.util import expand_ip, expand_port, choose_ephemeral_port
from scapy.all import IP, TCP

TCP_FLAG_MAP = {
    # FIN
    "FIN": "F",
    "FINISH": "F",

    # SYN
    "SYN": "S",
    "SYNC": "S",

    # RST
    "RST": "R",
    "RESET": "R",

    # PSH
    "PSH": "P",
    "PUSH": "P",

    # ACK
    "ACK": "A",
    "ACKNOWLEDGE": "A",

    # URG
    "URG": "U",
    "URGENT": "U",

    # ECN
    "ECE": "E",
    "ECN": "E",
    "ECHO": "E",

    # Congestion control
    "CWR": "C",
    "CONGESTION": "C",
    "CONTROL": "C"
}

def build_tcp_packet(intent, index=0):
    ip = IP(
        src=expand_ip(intent["src_ip"], index) if intent.get("src_ip") else None,
        dst=expand_ip(intent["dst_ip"], index),
        ttl=intent["ttl"] if intent.get("ttl") is not None else None
    )

    flags = "".join(TCP_FLAG_MAP[f.upper()] for f in intent["flags"])

    if intent.get("src_port") in (None, "random"):
        sport = choose_ephemeral_port()
    else:
        sport = expand_port(intent["src_port"], index)

    tcp = TCP(
        sport=sport,
        dport=expand_port(intent["dst_port"], index),
        flags=flags,
        seq=intent["seq"] if intent.get("seq") is not None else None,
        window=intent["window"] if intent.get("window") is not None else None
    )

    pkt = ip / tcp
    return pkt
