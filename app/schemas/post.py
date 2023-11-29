from datetime import datetime

from typing import Optional
from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class Post(PostBase):
    pass

class UpdatePost(PostBase):
    title: Optional[str]
    content: Optional[str]
    published: Optional[bool]


class PostCreate(PostBase):
    pass

class ResponsePost(PostBase):
    id:int
    created_at: datetime