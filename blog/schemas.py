from pydantic import BaseModel,Field
from typing import List, Optional

# class Blog(BaseModel):
#     title: str
#     body: str
#     user_id: Optional[int] = None

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True
    
class User(BaseModel):
    name:str
    email:str
    password: str = Field(..., max_length=72)
    
class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] =[]  
    class Config():
        orm_mode = True 
        
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Optional[ShowUser] = None
    class Config():
        orm_mode=True
        
        
class Login(BaseModel):
    username:str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None