from app.models import User


def test_user_creation():
    """Test User creation"""
    user = User(
        username="testuser", email="test@example.com", hashed_password="hashedpass"
    )
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.hashed_password == "hashedpass"


def test_user_representation():
    """Test User __str__ and __repr__ methods"""
    user = User(
        username="testuser", email="test@example.com", hashed_password="hashedpass"
    )
    assert str(user) == "testuser <test@example.com>"
    assert repr(user) == "<User(id=None, username=testuser, email=test@example.com)>"
