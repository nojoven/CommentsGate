"""This file contains helper functions."""
import uuid


def generate_uuid():
    return str(uuid.uuid4())

def is_timestamp(string: str):
   """
   Checks if publishedAt can be converted to float value.
   """
   try:
      float(string)
      return True
   except ValueError:
      return False


def trigger_eager_load(data):
   """
   Forces the ORM to load the children comments
 to prevent the absence of the replies in the response.
   """
   for comment in data:
      for reply in comment.replies:
         trigger_eager_load(reply.replies)