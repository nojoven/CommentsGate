from email import message
from enum import Enum
from fastapi import Depends, FastAPI, HTTPException, Path
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

import crud
from models import comment
from schemas.models import NewComment
from utils.helpers import is_timestamp, translate_en_to_fr, translate_fr_to_en
from database import SessionLocal, engine


comment.Base.metadata.create_all(bind=engine)


class LangName(str, Enum):
   fr = "fr"
   en = "en"


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/target/{targetId}/comments", responses={
   200: {"description": "comments matching targetId"},
   404: {"description": "Comment not found"}
})
async def get_target_comments(
   targetId: str = Path(..., summary="get all comments of a target."),
   skip: int = 0, limit: int = 100,
   db: Session = Depends(get_db)):
   """
   Get all comments of a target: 
   
   - **operationId** : targetComments
   - **description**: Get all comments of a target.
   """
   comments =  crud.get_target_comments(db, targetId, skip=skip, limit=limit)
   if not comments:
      raise HTTPException(404, detail="Comment not found.")


   return jsonable_encoder(comments)


@app.post("/target/{targetId}/comments", responses={
   200: {"description": "Comment created."}
   })
async def add_comment(
   comment: NewComment,
   targetId: str = Path(..., summary="Add comment on a target."),
   db: Session = Depends(get_db)):
   """
   Add comment on a target:

   - **operationId**: addComment
   """
   
   if not comment:
      raise HTTPException(status_code=422, detail="A comment is required.")

   if not comment.textFr and not comment.textEn:
      raise HTTPException(status_code=422, detail="A text is required at least in one language.")
   
   if comment.publishedAt and not is_timestamp(comment.publishedAt) :
      raise HTTPException(status_code=422, detail="The date field is not a valid timestamp.")

   if comment.textFr and not comment.textEn:
      comment.textEn = translate_fr_to_en(comment.textFr)
      message = f"'{comment.textFr}' => '{comment.textEn}'"

   if comment.textEn and not comment.textFr:
      comment.textFr = translate_en_to_fr(comment.textEn)
      message = f"'{comment.textFr}' => '{comment.textEn}'"
   
   new_comment = jsonable_encoder(crud.create_comment(db, comment))

   
   return new_comment
   # return jsonable_encoder(new_comment)