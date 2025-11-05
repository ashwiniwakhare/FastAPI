from pydantic import BaseModel,Field
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    user_id: Optional[int] = None
    
class ShowBlog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password: str = Field(..., max_length=72)
    
class ShowUser(BaseModel):
    name:str
    email:str
    