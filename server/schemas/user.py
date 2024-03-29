from pydantic import BaseModel


class UserModel(BaseModel):
    chat_id: int
    parameters: dict
