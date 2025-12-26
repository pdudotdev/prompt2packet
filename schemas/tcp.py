from typing import Optional, List, Literal, Union
from ipaddress import IPv4Address
from pydantic import Field
from schemas.base import BaseIntent
from config import MIN_PORT, MAX_PORT

class TCPIntent(BaseIntent):
    protocol: Literal["tcp"]

    dst_ip: IPv4Address
    dst_port: int = Field(ge=MIN_PORT, le=MAX_PORT)
    flags: List[Literal["FIN","SYN","RST","PSH","ACK","URG"]]

    src_ip: Optional[IPv4Address] = None
    src_port: Optional[Union[int, Literal["random"]]] = "random"
    
    seq: Optional[int] = None
    window: Optional[int] = None
    ttl: Optional[int] = None
