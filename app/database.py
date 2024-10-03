from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from . import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# pylint: disable=R0903
class Base(DeclarativeBase):
    """Base class for declarative_base"""

def get_db():
    """Obtain a database session

    Yields:
        Session: A database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
