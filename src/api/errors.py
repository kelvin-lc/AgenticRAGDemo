from typing import Any, Dict, Optional

from fastapi import HTTPException


class APIError(HTTPException):
    status_code = 400
    code = 10000
    message = "General API Error"

    def __init__(
        self,
        status_code: int = None,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        status_code = status_code or self.status_code
        detail = detail or {"code": self.code, "message": self.message}
        super().__init__(
            status_code=status_code,
            detail=detail,
        )
        self.headers = headers


class InvalidToken(APIError):
    status_code = 401
    code = 40010
    message = "Invalid Token"


class InternalError(APIError):
    status_code = 500
    code = 50010
    message = "Internal Error"
