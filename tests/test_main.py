import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Create a FastAPI test client."""
    with TestClient(app) as client:
        yield client


def test_root(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI!"}


def test_get_users(client):
    """Test get_users endpoint"""
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []
