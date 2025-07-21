from typing import Optional

from pydantic import BaseModel

from src.schemas.base import RequestBase


class AgentRequest(RequestBase):
    """Request model for an running an agent"""

    message: str = "李四的项目名称是什么"
    stream: bool = False
