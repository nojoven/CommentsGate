from datetime import datetime
import json
from fastapi.testclient import TestClient

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
   targetId_example = "Comment-kjh784fgevdhhdwhh7563"

   response = client.get(f"/target/{targetId_example}/comments")
   assert response.status_code == 200
   assert response.json() == True

def test_create_new_comment():
   targetId_example = "Comment-kjh784fgevdhhdwhh7563"
   comment = dict()
   comment["id"] = "opcrc-6575"
   comment["textFr"] = "Bien joué!"
   comment["textEn"] = "Well Done!"
   comment["publishedAt"] = str(datetime.now().timestamp())
   comment["authorId"] = "cjo8922"
   comment["targetId"] = targetId_example
   comment["replies"] = ["aaaa"]
   comment["isReply"] = False
   print(type(comment))
   response = client.post(
      f"/target/{targetId_example}/comments", 
      data=json.dumps(comment),
      headers={"Content-Type": "application/json"})
   assert response.status_code == 200