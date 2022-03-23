from typing import Optional

from sqlmodel import Field, SQLModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, relation

from database import Base
from pydantic import BaseModel

from .user import User



# class Comment(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     comment_id: str
#     targetId: str
#     textFr: str
#     textEn: str
#     publishedAt: str
#     authorId: str = Field(foreign_key= ForeignKey('users.author_id'))
#     targetId: str
#     replies: list[str] = []
#     isReply: bool = False


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    comment_id = Column(String, unique=True, index=True)
    textFr = Column(String, unique=True, index=True)
    textEn = Column(String, unique=True, index=True)
    publishedAt = Column(String, unique=True, index=True)
    authorId = Column(String, ForeignKey('users.author_id'))
    targetId = Column(String, unique=True, index=True)
    reply_id = Column(Integer, ForeignKey('comments.comment_id'))
    replies = relation("Comment", remote_side=[comment_id], uselist=True)

    author = relationship("User", back_populates="comments")
