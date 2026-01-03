from pydantic import BaseModel, Field
from ipaddress import IPv4Address

class IPRange(BaseModel):
    start: IPv4Address
    end: IPv4Address

    def __init__(self, **data):
        super().__init__(**data)

        if int(self.start) > int(self.end):
            raise ValueError("IPRange start must be <= end")

class PortRange(BaseModel):
    start: int = Field(ge=1, le=65535)
    end: int = Field(ge=1, le=65535)

    def __init__(self, **data):
        super().__init__(**data)

        if self.start > self.end:
            raise ValueError("PortRange start must be <= end")