from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    description: str
    content: str
    author: str

class User(BaseModel):
    username: str
    email: str
    full_name: str