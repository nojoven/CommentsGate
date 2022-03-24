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
    authorId = Column(String, ForeignKey('users.authorId'))
    targetId = Column(String, unique=True, index=True)
    replyId = Column(Integer, ForeignKey('comments.commentId'))
    replies = relation("Comment", remote_side=[commentId], uselist=True)

    author = relationship("User", back_populates="comments")
