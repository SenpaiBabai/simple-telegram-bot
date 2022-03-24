from pydantic import BaseModel, Field

from type.user import User
from type.chat import Chat

class Message(BaseModel):
    message_id: int
    from_who: User = Field(alias="from")
    chat: Chat
    date: int
    text: str