import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app  # Ensure this points to your FastAPI app module


@pytest.fixture
def client():
    with patch("app.main.check_connection"):
        yield TestClient(app)


def test_health_check(client):
    response = client.get("/ping")

    assert response.status_code == 200

    json_data = response.json()

    assert "code" in json_data
    assert isinstance(json_data["code"], int)
    assert json_data["msg"] == "pong"


# def test_health_check_with_error(client):
#     with patch("app.main.check_connection", side_effect=Exception("Mock error")):
#         response = client.get("/ping")

#         assert response.status_code == 500

#         json_data = response.json()
#         assert json_data == {"error": "Internal Server Error"}

