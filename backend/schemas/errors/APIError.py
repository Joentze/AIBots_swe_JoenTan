"""typing for APIError"""
from pydantic import BaseModel


class APIError(BaseModel):
    """type for APIError"""
    code: int
    message: str
    request: object
    details: object
