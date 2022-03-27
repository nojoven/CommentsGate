"""This file contains helper functions."""
import uuid
import requests

import detectlanguage
from deep_translator import DeeplTranslator

from fastapi import HTTPException

from settings import LANG_DETECTION_API_KEY, DEEPL_API_KEY
from .constants import DESTINATION_URL
from schemas.models import Comment

def generate_uuid():
    return str(uuid.uuid4())

def identify_language(text: str):
   return detectlanguage.single_detection(text, api_key=LANG_DETECTION_API_KEY)

def is_timestamp(string: str):
   """Checks if publishedAt can be converted to float value."""
   try:
      float(string)
      return True
   except ValueError:
      return False

def translate_en_to_fr(text: str):
   """Translates English text."""
   return DeeplTranslator(
      api_key=DEEPL_API_KEY, 
      source="en", target="fr", 
      use_free_api=True).translate(text)
   
def translate_fr_to_en(text: str):
   """Translates French text."""
   return DeeplTranslator(
      api_key=DEEPL_API_KEY, 
      source="fr", target="en", 
      use_free_api=True).translate(text)

def transmit_new_comment(new_comment: Comment, message: str):
   """Adapts and sends the new comment to another service."""
   transmittable_data = {
      "id": new_comment["id"],
      "publishedAt": new_comment["publishedAt"],
      "message": message,
      "author": new_comment["authorId"],
      "targetId": new_comment["targetId"],
      "replies": new_comment["replies"]
   }
   
   res = requests.post(DESTINATION_URL, transmittable_data)
   res.raise_for_status()


def trigger_eager_load(data):
   """
   Forces the ORM to load the children comments
 to prevent the absence of the replies in the response.
   """
   for comment in data:
      for reply in comment.replies:
         trigger_eager_load(reply.replies)
