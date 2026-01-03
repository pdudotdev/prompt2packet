from scapy.all import IP, UDP, Raw
from packet.util import choose_ephemeral_port

def build_udp_packet(template, index=0):
    ip = IP(dst=str(template["dst_ip"]))

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
