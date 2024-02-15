"""typing for Conversations"""
from typing import List
from pydantic import BaseModel
from schemas.Prompt import Prompt


class ConversationFull(BaseModel):
    """type for ConversationFull"""
    messages: List[Prompt]
