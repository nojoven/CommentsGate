from sqlalchemy.orm import Session

from .models import comment, user
from .schemas import models as pydantic_models

def get_comments_of_target(db: Session, targetId: str, skip: int = 0, limit: int = 200):
   return db.query(comment.Comment).filter(comment.Comment.targetId == targetId).offset(skip).limt(limit).all()


def create_comment(db: Session, comment: pydantic_models.NewComment):
   db_comment = comment.Comment(**comment.dict())
   db.add(db_comment)
   db.commit()
   db.refresh(db_comment)
   return db_comment