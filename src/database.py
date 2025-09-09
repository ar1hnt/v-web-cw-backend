from src.config import config

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    url=config.database_url_asyncpg,
    echo=False,
    pool_size=5,
    max_overflow=10
)

session_db = async_sessionmaker(engine, expire_on_commit=False)
