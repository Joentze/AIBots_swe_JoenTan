"""typings for prompt"""
from pydantic import BaseModel, Field
from schemas.QueryRole import QueryRoleType


class Prompt(BaseModel):
    """type for Prompt"""
    role: QueryRoleType = Field(...)
    content: str = Field(...)
