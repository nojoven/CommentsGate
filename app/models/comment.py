from datetime import datetime

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from utils.helpers import generate_uuid

from database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(
        String, unique=True, primary_key=True, index=True, default=generate_uuid
    )
    textFr = Column(String, index=True)
    textEn = Column(String, index=True)
    publishedAt = Column(
        String, nullable=False, default=str(datetime.now().timestamp()), index=True
    )
    authorId = Column(String, index=True)
    targetId = Column(
        String,
        index=True,
    )
    replies = relationship(
        "Comment",
        uselist=True,
        foreign_keys=[targetId],
        primaryjoin="Comment.id == Comment.targetId",
        lazy="subquery",
    )
