"""typing for Conversations"""
from beanie import Document
from pydantic import UUID4, Field


class Conversation(Document):
    """type for Conversation"""
    # id: UUID4 = Field(...)
    name: str = Field(..., max_length=200)
    params: object = Field(...)
    tokens: int = Field(..., ge=0)
