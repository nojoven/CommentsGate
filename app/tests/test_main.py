from datetime import datetime
import json
from fastapi.testclient import TestClient

from utils.constants import TARGET_ID_EXAMPLE as targetId_test
from app.main import app

client = TestClient(app)

def test_create_new_comment():
   comment = dict()
   comment["textFr"] = "Bien joué!"
   comment["textEn"] = "Well Done!"
   comment["publishedAt"] = str(datetime.now().timestamp())
   comment["authorId"] = "cjo2022"
   comment["targetId"] = targetId_test

   response = client.post(
      f"/target/{targetId_test}/comments", 
      data=json.dumps(comment),
      headers={"Content-Type": "application/json"})
   assert response.status_code == 200

def test_get_all_target_comments():
      response = client.get(f"/target/{targetId_test}/comments")
      assert response.status_code == 200
      assert isinstance(json.loads(response.content), list)
      assert "replies" in json.loads(response.content)[0].keys()