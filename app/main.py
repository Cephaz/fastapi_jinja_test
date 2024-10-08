from contextlib import asynccontextmanager

import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from alembic import command
from alembic.config import Config

from . import models, schemas
from .database import get_db


@asynccontextmanager
async def lifespan(_app : FastAPI):
    """Start the application lifespan."""
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

    yield

    # End the application lifespan.
    print("Shutting down")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    """Root endpoint.

    returns:
        dict: Welcome message

    """
    return {"message": """Welcome to FastAPI!"""}


@app.get("/users", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Get all users.

    Returns:
        dict: List of users

    """
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
