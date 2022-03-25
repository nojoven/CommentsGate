"""This file contains helper functions."""
import uuid


def trigger_eager_load(data):
   for comment in data:
      for reply in comment.replies:
         trigger_eager_load(reply.replies)

def generate_uuid():
    return str(uuid.uuid4())