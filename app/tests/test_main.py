from datetime import datetime
import json
from fastapi.testclient import TestClient

from utils.constants import TARGET_ID_EXAMPLE
from app.main import app


client = TestClient(app)


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

   response = client.post(
      f"/target/{TARGET_ID_EXAMPLE}/comments", 
      data=json.dumps(comment),
      headers={"Content-Type": "application/json"})
   assert response.status_code == 201