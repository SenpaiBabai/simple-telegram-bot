from pydantic import BaseModel

class User(BaseModel):
    id: int
    is_bot: bool
    username: str