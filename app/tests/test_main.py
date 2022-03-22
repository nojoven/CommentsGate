from fastapi import FastAPI
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
   response = client.get("/lang/fr/publish")
   assert response.status_code == 200
   assert response.json() is not None
   assert "Français" in  response.json()["message"]
