import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import models, schemas
from .database import get_db

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint.

    returns:
        dict: Welcome message

    """
    return {
        "message": """Welcome to FastAPI!"""
    }


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
