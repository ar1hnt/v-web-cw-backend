from src.database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, BigInteger, DateTime

from datetime import datetime


class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(length=256), nullable=False, unique=True)
    hashed_password: Mapped[int] = mapped_column(String, nullable=True) # Хэшированный пароль, nullable=True при OAuth 2.0
    username: Mapped[str] = mapped_column(String(length=30), nullable=True, unique=True)
    avater_url: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String(256), nullable=True)
    gender: Mapped[str] = mapped_column(String(length=10), nullable=False, default='не указан')
    telegram_contact: Mapped[str] = mapped_column(String(length=256), nullable=True)
    github_contact: Mapped[str] = mapped_column(String(length=256), nullable=True)
    leetcode_contact: Mapped[str] = mapped_column(String(length=256), nullable=True)
    stackoverlow_contact: Mapped[str] = mapped_column(String(length=256), nullable=True)
    first_name: Mapped[str] = mapped_column(String(length=256), nullable=False) # Имя
    surname: Mapped[str] = mapped_column(String(length=256), nullable=False) # Фамилия
    patronymic: Mapped[str] = mapped_column(String(length=256), nullable=True) # Отчество, если есть
    balance: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)

    happy_birthday: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)


class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256), nullable=False)
    text: Mapped[str]


class OAuthAccount(Base):
    __tablename__ = "oauth_accounts"

    ...