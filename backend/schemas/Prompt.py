"""typings for prompt"""
from pydantic import BaseModel
from schemas.QueryRole import QueryRoleType


class Prompt(BaseModel):
    """type for Prompt"""
    role: QueryRoleType
    content: str