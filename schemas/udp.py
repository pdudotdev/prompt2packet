from typing import Optional, List, Literal, Union
from ipaddress import IPv4Address
from pydantic import Field
from schemas.base import BaseIntent
from schemas.ranges import IPRange, PortRange

class UDPIntent(BaseIntent):
    protocol: Literal["udp"]

    dst_ip: Union[IPv4Address, IPRange]
    dst_port: Union[int, PortRange]

    src_ip: Optional[Union[IPv4Address, IPRange]] = None
    src_port: Optional[Union[int, PortRange, Literal["random"]]] = "random"

    payload: Optional[str] = None
