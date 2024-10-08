from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from app.schemas import User, UserBase


def test_user_base_schema():
    """Test user base schema."""
    user_data = {"username": "testuser", "email": "test@example.com"}
    user = UserBase(**user_data)
    assert user.username == "testuser"
    assert user.email == "test@example.com"


def test_user_base_schema_validation():
    """Test user base schema validation."""
    with pytest.raises(ValidationError):
        UserBase(username="", email="invalid_email")


def test_user_schema():
    """Test user schema."""
    user_data = {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
    }
    user = User(**user_data)
    assert user.id == 1
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert isinstance(user.created_at, datetime)
    assert isinstance(user.updated_at, datetime)


def test_user_schema_from_orm():
    """Test user schema from ORM using a dictionary."""
    orm_user_data = {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
    }

    # Validation du schéma directement à partir du dictionnaire
    user = User.model_validate(orm_user_data)

    # Assertions
    assert user.id == 1
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert isinstance(user.created_at, datetime)
    assert isinstance(user.updated_at, datetime)
