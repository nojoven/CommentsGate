from datetime import datetime
import uuid
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String

from sqlalchemy.orm import relationship

from database import Base

def generate_uuid():
    return str(uuid.uuid4())


class Comment(Base):
    __tablename__ = "comments"

    id = Column(String, unique=True, primary_key=True, index=True, default=generate_uuid)
    textFr = Column(String, index=True)
    textEn = Column(String, index=True)
    publishedAt = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now().timestamp(), index=True)
    authorId =  Column(String, index=True)
    targetId = Column(String, index=True,)
    replies =  relationship("Comment", uselist=True, foreign_keys=[targetId], primaryjoin="Comment.id == Comment.targetId", lazy='subquery')


