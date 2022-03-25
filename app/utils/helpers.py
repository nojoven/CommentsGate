"""This file contains helper functions."""
import uuid

from deep_translator import DeeplTranslator
import detectlanguage

from settings import LANG_DETECTION_API_KEY, DEEPL_API_KEY
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

def transmit_new_comment(new_comment: Comment):
   pass

def trigger_eager_load(data):
   """
   Forces the ORM to load the children comments
 to prevent the absence of the replies in the response.
   """
   for comment in data:
      for reply in comment.replies:
         trigger_eager_load(reply.replies)
