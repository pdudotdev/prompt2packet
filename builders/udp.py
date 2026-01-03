from scapy.all import IP, UDP, Raw
from builders.util import choose_ephemeral_port, expand_ip, expand_port

def build_udp_packet(intent, index=0):
    ip = IP(
        src=expand_ip(intent["src_ip"], index) if intent.get("src_ip") else None,
        dst=expand_ip(intent["dst_ip"], index)
    )

    # Destination port (mandatory)
    dport = expand_port(intent["dst_port"], index)

    # Source port handling
    src_port = intent.get("src_port")
    if src_port in (None, "random"):
        sport = choose_ephemeral_port()
    else:
        sport = src_port

    udp = UDP(sport=sport, dport=dport)

    pkt = ip / udp

    if intent.get("payload"):
        pkt = pkt / Raw(load=intent["payload"].encode())

    return pkt
