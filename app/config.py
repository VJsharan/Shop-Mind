"""
ShopMind Application Configuration.

Loads environment variables via pydantic-settings and python-dotenv.
Exports a singleton `settings` instance used across the application.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables and .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    GCP_PROJECT_ID: str
    VERTEX_LOCATION: str = "asia-south1"
    FIRESTORE_DATABASE: str = "newdb"
    GOOGLE_APPLICATION_CREDENTIALS: str | None = None


settings: Settings = Settings()
