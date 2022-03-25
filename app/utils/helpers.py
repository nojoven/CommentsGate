"""This file contains helper functions."""
import uuid

from deep_translator import DeeplTranslator


def generate_uuid():
    return str(uuid.uuid4())

def is_french_text(text: str):
   pass

def is_english_text(text: str):
   pass

def is_timestamp(string: str):
   """
   Checks if publishedAt can be converted to float value.
   """
   try:
      float(string)
      return True
   except ValueError:
      return False

def translate_en_to_fr(text: str):
   """Translates English text."""
   return DeeplTranslator(source='en', target='fr').translate(text)
   
def translate_fr_to_en(text: str):
   """Translates French text."""
   return DeeplTranslator(source='fr', target='en').translate(text)

def trigger_eager_load(data):
   """
   Forces the ORM to load the children comments
 to prevent the absence of the replies in the response.
   """
   for comment in data:
      for reply in comment.replies:
         trigger_eager_load(reply.replies)
