from schemas.tcp import TCPIntent
from schemas.udp import UDPIntent
from packet.tcp import build_tcp_packet
from packet.udp import build_udp_packet

PROTOCOLS = {
    "tcp": {
        "schema": TCPIntent,
        "builder": build_tcp_packet,
    },
    "udp": {
        "schema": UDPIntent,
        "builder": build_udp_packet,
    },
}
