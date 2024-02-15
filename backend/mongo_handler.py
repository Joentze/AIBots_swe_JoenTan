"""handlers for mongodb"""
from schemas.Conversation import ConversationFull
from schemas.Prompt import Prompt


async def add_to_message_history(id: str, prompt: Prompt) -> None:
    """adds message history to the message field"""
    doc = await ConversationFull.get(id)
    response = await doc.set({ConversationFull.messages: [*doc.messages, prompt]})
    print(response)
