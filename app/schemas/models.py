from typing import Optional

from pydantic import BaseModel


class CommentBase(BaseModel):
   commentId: str
   targetId: str
   textFr: str
   textEn: str
   publishedAt: str
   authorId: str
   targetId: str


class CommentCreate(CommentBase):
   pass

class Comment(CommentBase):
   id: Optional[int]
   replies: list[str] = []

   
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
