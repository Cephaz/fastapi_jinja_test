from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    """User base schema."""

    username: str = Field(..., min_length=1, max_length=50)
    email: EmailStr = Field(..., max_length=100)


class User(UserBase):
    """User schema."""

    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
