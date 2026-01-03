from typing import Optional, Literal, Union
from ipaddress import IPv4Address
from pydantic import BaseModel, Field
from schemas.ranges import IPRange, PortRange
from config import DEF_PACKETS, MAX_PACKETS, DEF_INTERVAL_MS, MAX_INTERVAL_MS

class UDPIntent(BaseModel):
    protocol: Literal["udp"] = "udp"

    count: int = Field(default=DEF_PACKETS, ge=1, le=MAX_PACKETS)
    interval_ms: int = Field(default=DEF_INTERVAL_MS, ge=0, le=MAX_INTERVAL_MS)

    dst_ip: Union[IPv4Address, IPRange]
    dst_port: Union[int, PortRange]

    src_ip: Optional[Union[IPv4Address, IPRange]] = None
    src_port: Optional[Union[int, PortRange, Literal["random"]]] = "random"
