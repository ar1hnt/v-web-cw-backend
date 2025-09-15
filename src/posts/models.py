from typing import TYPE_CHECKING

from src.utils import current_time
from src.database import Base

if TYPE_CHECKING:
    from src.auth.models import User
    from src.comments.models import Comment

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, ForeignKey, String, DateTime, Text

from datetime import datetime


class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(length=256), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    is_news: Mapped[bool] = mapped_column(Boolean, default=False)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=current_time)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True, onupdate=current_time)

    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    post_likes = relationship("PostLikes", back_populates="post", cascade="all, delete-orphan")


class PostLikes(Base):
    __tablename__ = "post_likes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=current_time)

    user = relationship("User", back_populates="post_likes")
    post = relationship("Post", back_populates="post_likes")