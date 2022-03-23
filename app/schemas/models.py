from typing import Optional

from sqlmodel import Field, SQLModel

from pydantic import BaseModel


class Comment(BaseModel):
   id: int
   comment_id: str
   targetId: str
   textFr: str
   textEn: str
   publishedAt: str
   authorId: str
   targetId: str
   replies: list[str] = []
   isReply: bool = False

   class Config:
      orm_mode = True

class User(BaseModel):
   id: int
   authorId: str
   comments: list[Comment] = []

   class Config:
      orm_mode = True

