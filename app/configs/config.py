from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    ENV: str
    LOG_LEVEL: str
    DB_URL: str

    model_config = SettingsConfigDict(env_file=".env")
