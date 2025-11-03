from typing import Final

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    OAUTH_GOOGLE_CLIENT_ID: Final[str]
    OAUTH_GOOGLE_CLIENT_SECRET: Final[str]

    DB_POSTGRESQL_HOST: Final[str]
    DB_POSTGRESQL_PORT: Final[int]
    DB_POSTGRESQL_USER: Final[str]
    DB_POSTGRESQL_PASS: Final[str]
    DB_POSTGRESQL_NAME: Final[str]

    @property
    def database_url_asyncpg(self):
        """Ссылка на базу данных с asyncpg движком"""
        return f"postgresql+asyncpg://{self.DB_POSTGRESQL_USER}:{self.DB_POSTGRESQL_PASS}@{self.DB_POSTGRESQL_HOST}:{self.DB_POSTGRESQL_PORT}/{self.DB_POSTGRESQL_NAME}"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", validate_default=True)


settings = Config() # type: ignore