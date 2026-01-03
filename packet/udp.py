from scapy.all import IP, UDP, Raw
from packet.util import choose_ephemeral_port, expand_ip

def build_udp_packet(template, index=0):
    ip = IP(
        src=expand_ip(template["src_ip"], index) if template.get("src_ip") else None,
        dst=expand_ip(template["dst_ip"], index)
    )

    # Destination port (mandatory)
    dport = template["dst_port"]

    # Source port handling
    src_port = template.get("src_port")
    if src_port in (None, "random"):
        sport = choose_ephemeral_port()
    else:
        sport = src_port

    udp = UDP(sport=sport, dport=dport)

    pkt = ip / udp

    if template.get("payload"):
        pkt = pkt / Raw(load=template["payload"].encode())

    return pkt
