
from typing import Optional, List
from pydantic import BaseModel


class CommentBase(BaseModel):
   id: Optional[str]
   targetId: Optional[str]
   textFr: Optional[str]
   textEn: Optional[str]
   publishedAt: Optional[str]
   authorId: Optional[str]
   

class NewComment(CommentBase):
   pass

class Comment(CommentBase):
   id: str | None
   replies: list #dict #List = [] # list[dict] = []
   
   class Config:
      orm_mode = True
