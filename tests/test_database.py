import pytest
from sqlalchemy.engine.url import make_url
from sqlalchemy.orm import DeclarativeBase, Session

from app import config
from app.database import Base, SessionLocal, engine, get_db


def test_engine_creation():
    """Test engine creation"""
    config_url = make_url(config.SQLALCHEMY_DATABASE_URL)
    engine_url = make_url(engine.url)

    assert config_url.drivername == engine_url.drivername
    assert config_url.username == engine_url.username
    assert config_url.password == engine_url.password
    assert config_url.host == engine_url.host
    assert config_url.port == engine_url.port
    assert config_url.database == engine_url.database


def test_session_local():
    """Test SessionLocal"""
    assert isinstance(SessionLocal(), Session)


def test_base_class():
    """Test Base class"""
    assert issubclass(Base, DeclarativeBase)


def test_get_db():
    """Test get_db"""
    db = next(get_db())
    assert isinstance(db, Session)
    db.close()


@pytest.fixture
def mock_db_session(mocker):
    """Mock SessionLocal"""
    mock = mocker.patch("app.database.SessionLocal")
    mock.return_value = mocker.Mock(spec=Session)
    return mock


# pylint: disable=redefined-outer-name
def test_get_db_yield_and_close(mock_db_session):
    """Test get_db yield and close"""
    db = next(get_db())
    assert db == mock_db_session.return_value
    db.close.assert_called_once()
