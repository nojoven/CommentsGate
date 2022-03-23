from enum import Enum
from fastapi import FastAPI, HTTPException, Request, Form, Path
from fastapi.encoders import jsonable_encoder
from schemas.models import Comment


class LangName(str, Enum):
   fr = "fr"
   en = "en"


app = FastAPI()


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


@app.get("/target/{targetId}/comments")
async def targetComments(targetId: str = Path(..., 
summary="get all comments of a target.")):
   """
   Get all comments of a target: 
   
   - **operationId** : targetComments
   - **description**: Get all comments of a target.
   """
   return True


@app.post("/target/{targetId}/comments", status_code=201)
async def addComment(comment: Comment, targetId: str= Path(
   ..., 
   summary="Add comment on a target.")):
   """
   Add comment on a target:

   - **operationId**: addComment.
   """
   if not comment:
      raise HTTPException(status_code=422, detail="A comment is required.")

   return jsonable_encoder(comment)