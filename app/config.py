import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load .env file
load_dotenv()

# DB settings
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB")


class Settings(BaseSettings):
    """Settings for the application."""

    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = True
    API_KEY: str = os.getenv("API_KEY", "default_api_key")
    DATABASE_URL: str = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:"
        f"{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    @classmethod
    def get_settings(cls) -> "Settings":
        """Get the settings."""
        env = os.getenv("ENV", "development")
        if env == "production":
            return ProductionSettings()
        if env == "test":
            return TestSettings()
        return DevelopmentSettings()


class DevelopmentSettings(Settings):
    """Development settings."""

    ENV: str = "development"
    DEBUG: bool = True
    DATABASE_URL: str = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:"
        f"{POSTGRES_PORT}/{POSTGRES_DB}_development"
    )


class TestSettings(Settings):
    """Test settings."""

    ENV: str = "test"
    DEBUG: bool = True
    DATABASE_URL: str = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:"
        f"{POSTGRES_PORT}/{POSTGRES_DB}_test"
    )


class ProductionSettings(Settings):
    """Production settings."""

    DEBUG: bool = False
    DATABASE_URL: str = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:"
        f"{POSTGRES_PORT}/{POSTGRES_DB}_production"
    )


settings = Settings.get_settings()
