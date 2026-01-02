from pydantic import BaseModel, Field
from config import DEF_PACKETS, MAX_PACKETS, DEF_INTERVAL_MS, MAX_INTERVAL_MS

class BaseIntent(BaseModel):
    protocol: str
    count: int = Field(default=DEF_PACKETS, ge=DEF_PACKETS, le=MAX_PACKETS)
    interval_ms: int = Field(default=DEF_INTERVAL_MS, ge=0, le=MAX_INTERVAL_MS)
