import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from sqlalchemy.orm import relationship, relation

from database import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), unique=True, primary_key=True, index=True, default=uuid.uuid4)
    textFr = Column(String, index=True)
    textEn = Column(String, index=True)
    publishedAt = Column(String, index=True)
    authorId =  Column(String, index=True)  # Column(String, ForeignKey('users.authorId'), unique=True)
    targetId = Column(String, index=True)
    #childId = Column(String, ForeignKey('comments.id'))
    #replies =  relationship("Comment", uselist=True) #Column(MutableList.as_mutable(PickleType), default=[]) #


