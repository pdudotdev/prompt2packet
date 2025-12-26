from scapy.all import IP, UDP, Raw

def build_udp_packet(template):
    ip = IP(dst=str(template["dst_ip"]))
    udp = UDP(dport=template["dst_port"])

    if template.get("src_port"):
        udp.sport = template["src_port"]

    pkt = ip / udp

    if template.get("payload"):
        pkt = pkt / Raw(load=template["payload"].encode())

    return pkt
