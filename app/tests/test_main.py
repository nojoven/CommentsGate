from datetime import datetime
import json
from fastapi.testclient import TestClient

from ..utils.constants import TARGET_ID_EXAMPLE
from app.main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_select_language():
   """Testing the French path"""
   response = client.get("/lang/fr/publish")
   assert response.status_code == 200
   assert response.json() is not None
   assert "Français" in  response.json()["message"]

   """Testing the English path"""
   response = client.get("/lang/en/publish")
   assert response.status_code == 200
   assert response.json() is not None
   assert "English" in  response.json()["message"]

def test_get_all_target_comments():
   targetId = TARGET_ID_EXAMPLE

   response = client.get(f"/target/{targetId}/comments")
   assert response.status_code == 200
   assert response.json() == True

def test_create_new_comment():
   comment = dict()
   comment["id"] = "opcrc-6575"
   comment["textFr"] = "Bien joué!"
   comment["textEn"] = "Well Done!"
   comment["publishedAt"] = str(datetime.now().timestamp())
   comment["authorId"] = "cjo8922"
   comment["targetId"] = TARGET_ID_EXAMPLE
   comment["replies"] = ["aaaa"]
   comment["isReply"] = False
   print(comment)
   response = client.post(
      f"/target/{TARGET_ID_EXAMPLE}/comments", 
      data=json.dumps(comment),
      headers={"Content-Type": "application/json"})
   assert response.status_code == 201