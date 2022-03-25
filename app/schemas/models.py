
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class CommentBase(BaseModel):
   id: Optional[UUID]
   targetId: Optional[str]
   textFr: Optional[str]
   textEn: Optional[str]
   publishedAt: Optional[str]
   authorId: Optional[str]
   #replies: list[str] = []
   #childId: Optional[str]


class NewComment(CommentBase):
   pass

class Comment(CommentBase):
   id: str
   
   
   class Config:
      orm_mode = True

class UserBase(BaseModel):
   authorId: str
   

class UserCreate(UserBase):
   pass

class User(UserBase):
   id: int
   comments: list[Comment] = []

   class Config:
      orm_mode = True
