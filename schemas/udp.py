from typing import Optional, Literal
from ipaddress import IPv4Address
from pydantic import Field
from schemas.base import BaseIntent
from config import MIN_PORT, MAX_PORT

class UDPIntent(BaseIntent):
    protocol: Literal["udp"]

    dst_ip: IPv4Address
    dst_port: int = Field(ge=MIN_PORT, le=MAX_PORT)

    src_port: Optional[int] = None

    payload: Optional[str] = None
