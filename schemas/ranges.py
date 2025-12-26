from pydantic import BaseModel, Field
from ipaddress import IPv4Address
from typing import Optional

class IPRange(BaseModel):
    start: IPv4Address
    end: IPv4Address

class PortRange(BaseModel):
    start: int = Field(ge=1, le=65535)
    end: int = Field(ge=1, le=65535)
