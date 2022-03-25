from enum import Enum
from fastapi import Depends, FastAPI, HTTPException, Request, Form, Path
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

import crud
from models import comment
from schemas.models import Comment, NewComment

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


@app.get("/")
async def home():
   return {"message": "Hello World"}

@app.get("/lang/{lang_name}/publish")
async def select_language(lang_name: LangName):
   if lang_name == LangName.fr:
      return {"lang_name": lang_name, "message": "Publiez en Français"}

   if lang_name == LangName.en:
      return {"lang_name": lang_name, "message": "Publish in English"}

   return {"model_name": lang_name, "message": "ERROR"}


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


   return comments


@app.post("/target/{targetId}/comments", responses={
   200: {"description": "Comment created."}
   })
async def add_comment(
   comment: NewComment,
   targetId: str = Path(..., summary="Add comment on a target."),
   db: Session = Depends(get_db)):
   """
   Add comment on a target:

   - **operationId**: addComment.
   """
   if not comment:
      raise HTTPException(status_code=422, detail="A comment is required.")

   new_comment = crud.create_comment(db, comment)

  


   return jsonable_encoder(new_comment)