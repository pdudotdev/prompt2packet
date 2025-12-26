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

def build_tcp_packet(template):
    ip = IP(
    dst=str(template["dst_ip"]),
    src=str(template["src_ip"]) if template.get("src_ip") else None
    )

    flags = "".join(TCP_FLAG_MAP[f] for f in template["flags"])

    tcp = TCP(
        dport=template["dst_port"],
        flags=flags
    )

    if template.get("src_port") not in (None, "random"):
        tcp.sport = template["src_port"]

    if template.get("seq") is not None:
        tcp.seq = template["seq"]

    return ip / tcp
