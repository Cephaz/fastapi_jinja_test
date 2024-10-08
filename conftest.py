import pytest
from sqlalchemy.orm import Session

from alembic import command
from alembic.config import Config
from app.database import get_db


@pytest.fixture(scope="function")
def apply_migrations():
    """Fixture to apply Alembic migrations before running tests."""
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    yield
    command.downgrade(alembic_cfg, "base")


@pytest.fixture(scope="function")
def db_session(apply_migrations) -> Session:
    """Fixture to create a database session."""
    session = next(get_db())
    try:
        yield session
    finally:
        session.close()
