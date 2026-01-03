from typing import Optional, List, Literal, Union
from ipaddress import IPv4Address
from pydantic import Field, field_validator
from schemas.base import BaseIntent
from schemas.ranges import IPRange, PortRange

class UDPIntent(BaseIntent):
    protocol: Literal["udp"]

    dst_ip: Union[IPv4Address, IPRange]
    dst_port: Union[int, PortRange]

    src_ip: Optional[Union[IPv4Address, IPRange]] = None
    src_port: Optional[Union[int, PortRange, Literal["random"]]] = "random"

    payload: Optional[str] = None

    @field_validator("dst_port", "src_port", mode="before")
    @classmethod
    def validate_ports(cls, v):
        if isinstance(v, int):
            if not (1 <= v <= 65535):
                raise ValueError("Port must be between 1 and 65535")
        return v
