from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # MongoDB connection settings
    MONGODB_URL: str = "mongodb://root:example@localhost:27017"  # Default MongoDB URL
    MONGODB_DB: str = "test_db"  # Default database name

    class Config:
        # Allows loading from environment variables
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instantiate the settings object
settings = Settings()
