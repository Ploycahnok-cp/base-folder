from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: str = "dev"
    LOG_LEVEL: str = "info"
    DB_URL: str = "localhost:5432"

    model_config = SettingsConfigDict(env_file=".env")


async def get_settings() -> Settings:
    """
    Returns the Settings object.

    The Settings object is created by Pydantic's Settings class, which reads
    configuration from environment variables and a .env file.

    The .env file is expected to be in the root of the project and is used to
    configure the application.

    The Settings object is cached so that it is only created once and then
    reused for subsequent calls to this function.

    Returns:
        Settings: The Settings object.
    """
    return Settings()
