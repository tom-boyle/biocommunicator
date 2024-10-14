from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Biocommunicator API"}

def test_interpret_signal():
    response = client.get("/api/v1/interpret_signal")
    assert response.status_code == 200
    assert response.json() == {"message": "This is where AI model processing will happen"}