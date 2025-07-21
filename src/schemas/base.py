from typing import Optional

from pydantic import BaseModel


class RequestBase(BaseModel):
    """Base request model"""

    user_id: Optional[str] = None
    session_id: Optional[str] = None
