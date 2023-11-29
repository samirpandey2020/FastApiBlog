
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Boolean, DateTime


from .database import Base



class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="True", nullable=False)
    created_at = Column(
        DateTime, server_default=func.now(), nullable=False)
    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    user = Column(String, nullable=False, unique= False)
    email = Column(String, nullable= False, unique=True)
    password = Column(String, nullable=False)
    created_at= Column(DateTime,server_default=func.now(), nullable=False)

