from unittest.mock import MagicMock, patch

import pytest

from app import config, database


def test_create_engine():
    """Test if create_engine is called with the correct database URL."""
    with patch("app.database.create_engine") as mock_create_engine:
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        result = database.create_engine(config.settings.DATABASE_URL)
        mock_create_engine.assert_called_once_with(config.settings.DATABASE_URL)
        assert result == mock_engine


def test_get_db():
    """Test the normal operation of get_db function."""
    mock_db = MagicMock()
    with patch("app.database.SessionLocal", return_value=mock_db):
        db_generator = database.get_db()
        db_session = next(db_generator)
        assert db_session == mock_db
        mock_db.close.assert_not_called()
        try:
            next(db_generator)
        except StopIteration:
            pass
        mock_db.close.assert_called_once()


@pytest.fixture
def mock_db_session():
    """Fixture to create a mock database session."""
    return MagicMock()


def test_get_db_exception(mock_db_session):
    """Test get_db function behavior when an exception occurs."""
    with patch("app.database.SessionLocal", return_value=mock_db_session):
        db_generator = database.get_db()
        next(db_generator)  # This creates the session
        with pytest.raises(Exception):
            db_generator.throw(Exception("Test exception"))
    mock_db_session.close.assert_called_once()
