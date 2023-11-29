from datetime import datetime

from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    user: str
    password: str
    email: EmailStr

class ResponseUser(BaseModel):
    id: int
    user: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True