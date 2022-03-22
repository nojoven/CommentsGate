from enum import Enum
from fastapi import FastAPI

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
