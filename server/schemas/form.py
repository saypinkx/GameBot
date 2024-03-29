from pydantic import BaseModel
from bson.objectid import ObjectId


class FormCreate(BaseModel):
    chat_id: int
    first_name: str
    last_name: str
    age: str
    tag: str
    link_tg: str


class FormResponse(BaseModel):
    _id: str
    chat_id: int
    first_name: str
    last_name: str
    age: str
    tag: str
    link_tg: str
