from datetime import datetime

import pytest

from app.models import User


def test_user_creation(db_session):
    """Test user creation."""
    user = User(
        username="testuser", email="test@example.com", hashed_password="hashedpass"
    )
    db_session.add(user)
    db_session.commit()

    assert user.id is not None
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.hashed_password == "hashedpass"
    assert isinstance(user.created_at, datetime)
    assert isinstance(user.updated_at, datetime)


def test_user_representation():
    """Test user representation."""
    user = User(
        id=1,
        username="testuser",
        email="test@example.com",
        hashed_password="hashedpass",
    )
    assert str(user) == "testuser <test@example.com>"
    assert repr(user) == "<User(id=1, username=testuser, email=test@example.com)>"


def test_user_unique_constraint(db_session):
    """Test user unique constraint."""
    user1 = User(
        username="uniqueuser", email="unique@example.com", hashed_password="hashedpass"
    )
    db_session.add(user1)
    db_session.commit()

    user2 = User(
        username="uniqueuser", email="another@example.com", hashed_password="hashedpass"
    )
    db_session.add(user2)
    with pytest.raises(Exception):
        db_session.commit()
