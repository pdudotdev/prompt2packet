from typing import Optional, List, Literal, Union
from ipaddress import IPv4Address
from pydantic import Field
from schemas.base import BaseIntent
from schemas.ranges import IPRange, PortRange
from config import MIN_PORT, MAX_PORT

class TCPIntent(BaseIntent):
    protocol: Literal["tcp"]

    dst_ip: Union[IPv4Address, IPRange]
    dst_port: Union[int, PortRange]

    src_ip: Optional[Union[IPv4Address, IPRange]] = None
    src_port: Optional[Union[int, PortRange, Literal["random"]]] = "random"

    flags: List[Literal["FIN","SYN","RST","PSH","ACK","URG","ECE","CWR"]]
    
    seq: Optional[int] = None
    window: Optional[int] = None
    ttl: Optional[int] = None
