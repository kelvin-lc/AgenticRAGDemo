from typing import Optional

from pydantic import BaseModel

from src.schemas.base import RequestBase


class AgentRequest(RequestBase):
    """Request model for an running an agent"""

    message: str
    stream: bool = False
