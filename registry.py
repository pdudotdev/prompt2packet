from builders.tcp import build_tcp_packet
from builders.udp import build_udp_packet

# This script answers the question: Given a protocol, how do I build a packet?
PROTOCOLS = {
    "tcp": build_tcp_packet,
    "udp": build_udp_packet,
}
