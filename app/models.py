import datetime

from sqlalchemy import Column, DateTime, Integer, String, text

from .database import Base


class User(Base):
    """User is used for authentication

    Attributes:
        id (int): Unique identifier for the user.
        username (str): Unique username for the user. Max length 50 characters
        email (str): User's email address. Must be unique. Max length 100 characters
        hashed_password (str): Hashed version of the user's password. Max length 100 characters
        created_at (datetime): Timestamp of when the user account was created
        updated_at (datetime): Timestamp of when the user account was last updated

    Note:
        - The `hashed_password` should never store plain text passwords
        - Always use a secure hashing algorithm (e.g., bcrypt) to hash passwords before storing
        - The `updated_at` field is automatically updated whenever the user record is modified
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=datetime.datetime.now(datetime.timezone.utc),
    )

    def __str__(self):
        return f"{self.username} <{self.email}>"

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
