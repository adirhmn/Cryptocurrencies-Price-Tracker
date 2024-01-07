from pydantic import BaseModel
from typing import Any

class SuccessResponse(BaseModel):
    code: int = 200
    status: str = "success"
    data: Any
