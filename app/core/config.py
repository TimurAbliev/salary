from os import environ

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USER = environ.get("POSTGRES_USER", "postgres")
    DB_PASSWORD = environ.get("POSTGRES_PASSWORD", "postgres")
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_NAME = environ.get("DB_NAME", "postgres")
    DB_PORT = environ.get("DB_PORT", "5432")
    DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


settings = Settings()
