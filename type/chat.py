from pydantic import BaseModel

class Chat(BaseModel):
    id: int
    username: str