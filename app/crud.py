from sqlalchemy.orm import Session

from models import comment
from schemas import models as pydantic_models

from utils.helpers import trigger_eager_load


def get_target_comments(db: Session, targetId: str, skip: int = 0, limit: int = 200):
    data = (
        db.query(comment.Comment)
        .filter(comment.Comment.targetId == targetId)
        .offset(skip)
        .limit(limit)
        .all()
    )
    trigger_eager_load(data)
    return data


def create_comment(db: Session, NewComment: pydantic_models.NewComment):
    db_comment = comment.Comment(**NewComment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
