from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str  # Must match exactly with .env variable name

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


# Test the configuration
if __name__ == "__main__":
    settings = Settings()
    print(f"Database configuration loaded: {settings.DATABASE_URL[:20]}...")  # Print first 20 chars for security