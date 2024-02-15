"""typing for Conversations"""
from typing import List
from schemas.Prompt import Prompt
# from pydantic import BaseModel
from beanie import Document
from pydantic import Field


class Conversation(Document):
    """type for Conversation"""
    # id: UUID4 = Field(...)
    name: str = Field(..., max_length=200)
    params: object = Field(...)
    tokens: int = Field(..., ge=0)

    def to_json(self):
        """converts to json"""
        return {"id": str(self.id), "name": self.name, "params": self.params, "tokens": self.tokens}


class ConversationFull(Document):
    """type for ConversationFull"""
    messages: List[Prompt]

    def to_json(self):
        """converts to json"""
        return {"messages": self.messages}
