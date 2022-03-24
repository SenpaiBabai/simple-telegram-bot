from pydantic import BaseModel

from type.message import Message


class Event(BaseModel):
    update_id: int
    message: Message