from datetime import datetime

from typing import Optional
from uuid import uuid5

from pydantic import BaseModel


class Comment(BaseModel):
    id: str
    targetId: str
    textFr: str
    textEn: str
    publishedAt: str
    authorId: str
    targetId: str
    replies: Optional[list] = None
    isReply: Optional[bool] = False
