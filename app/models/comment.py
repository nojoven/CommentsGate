from datetime import datetime

from typing import Optional
from uuid import uuid5

from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    targetId: str
    textFr: str
    textEn: str
    publishedAt: datetime
    authorId: str
    targetId: str
    replies: list
    isReply: bool
