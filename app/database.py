from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from .config import settings


def init_db(db_url):
    """Initialize the database if it doesn't exist."""
    if not database_exists(db_url):
        create_database(db_url)
        print(f"Database created: {db_url}")


# Initialize the database
init_db(settings.DATABASE_URL)

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


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
