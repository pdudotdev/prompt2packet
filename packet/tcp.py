from scapy.all import IP, TCP

def build_tcp_packet(template):
    ip = IP(dst=str(template["dst_ip"]))
    tcp = TCP(
        dport=template["dst_port"],
        flags="".join(template["flags"])
    )

    if template.get("src_port") not in (None, "random"):
        tcp.sport = template["src_port"]

    if template.get("seq") is not None:
        tcp.seq = template["seq"]

    return ip / tcp
