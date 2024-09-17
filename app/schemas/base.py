from typing import Any

from pydantic import BaseModel


class ResponseBase(BaseModel):
    msg: str = "ok"
    data: Any = None
    code: int = 200
