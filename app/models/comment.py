from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, relation

from database import Base

from .user import User

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    commentId = Column(String, unique=True, index=True)
    textFr = Column(String, unique=True, index=True)
    textEn = Column(String, unique=True, index=True)
    publishedAt = Column(String, unique=True, index=True)
    authorId = Column(String, ForeignKey('users.author_id'))
    targetId = Column(String, unique=True, index=True)
    reply_id = Column(Integer, ForeignKey('comments.comment_id'))
    replies = relation("Comment", remote_side=[comment_id], uselist=True)

    author = relationship("User", back_populates="comments")
