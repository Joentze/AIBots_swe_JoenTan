"""typing for Conversations"""
from pydantic import BaseModel, UUID4, Field


class Conversation(BaseModel):
    """type for Conversation"""
    id: UUID4 = Field(...)
    name: str = Field(max_length=200)
    params: dict = Field(...)
    tokens: int = Field(ge=0)
