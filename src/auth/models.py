from typing import TYPE_CHECKING

from src.utils import current_time
from src.database import Base

if TYPE_CHECKING:
    from src.posts.models import Post, PostLikes
    from src.comments.models import Comment, CommentLikes

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, BigInteger, DateTime, UniqueConstraint

from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(length=256), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=True) # Хэшированный пароль, nullable=True при OAuth
    username: Mapped[str] = mapped_column(String(length=30), nullable=True, unique=True)
    avatar_url: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String(length=256), nullable=True)
    gender: Mapped[str] = mapped_column(String(length=10), nullable=False, default='не указан')
    telegram_contact: Mapped[str] = mapped_column(String(length=256), nullable=True)
    github_contact: Mapped[str] = mapped_column(String(length=256), nullable=True)
    leetcode_contact: Mapped[str] = mapped_column(String(length=256), nullable=True)
    stackoverflow_contact: Mapped[str] = mapped_column(String(length=256), nullable=True)
    first_name: Mapped[str] = mapped_column(String(length=256), nullable=False) # Имя
    surname: Mapped[str] = mapped_column(String(length=256), nullable=False) # Фамилия
    patronymic: Mapped[str] = mapped_column(String(length=256), nullable=True) # Отчество, если есть
    balance: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)

    happy_birthday: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=current_time)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True, onupdate=current_time)

    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="author", cascade="all, delete-orphan")
    post_likes = relationship("PostLikes", back_populates="user", cascade="all, delete-orphan")
    comment_likes = relationship("CommentLikes", back_populates="user", cascade="all, delete-orphan")


class OAuthAccount(Base):
    __tablename__ = "oauth_accounts"
    __table_args__ = (UniqueConstraint("provider", "provider_user_id", name="uq_provider_user"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    provider: Mapped[str] = mapped_column(String(length=256), nullable=False)
    provider_user_id: Mapped[str] = mapped_column(String(length=256), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=current_time)
