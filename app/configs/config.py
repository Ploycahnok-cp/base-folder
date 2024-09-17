from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: str
    LOG_LEVEL: str
    DB_URL: str

    model_config = SettingsConfigDict(env_file=".env")


async def get_settings() -> Settings:
    return Settings()