from packet.util import expand_ip, expand_port, choose_ephemeral_port
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

def build_tcp_packet(template, index=0):
    ip = IP(
        src=expand_ip(template["src_ip"], index) if template.get("src_ip") else None,
        dst=expand_ip(template["dst_ip"], index)
    )

    flags = "".join(TCP_FLAG_MAP[f.upper()] for f in template["flags"])

    if template.get("src_port") in (None, "random"):
        sport = choose_ephemeral_port()
    else:
        sport = expand_port(template["src_port"], index)

    tcp = TCP(
        sport=sport,
        dport=expand_port(template["dst_port"], index),
        flags=flags
    )

    pkt = ip / tcp
    return pkt
