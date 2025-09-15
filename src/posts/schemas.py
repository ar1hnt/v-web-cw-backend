from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from datetime import datetime

from src.auth.schemas import UserRead
from src.comments.schemas import CommentRead


# POST -------------------------------------
class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=256)
    text: str = Field(min_length=1)
    is_news: Optional[bool] = Field(default=False, description="Является ли пост новостным. Только для администраторов")


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    created_at: datetime
    author: UserRead
    comments: List[CommentRead] = []
    likes_count: int = 0

    model_config = ConfigDict(from_attributes=True)


class PostUpdate(BaseModel):
    title: Optional[str] = Field(min_length=1, max_length=256)
    text: Optional[str] = Field(min_length=1)
    is_news: Optional[bool]
# ------------------------------------------


# POST LIKES -------------------------------
class PostLikeCreate(BaseModel):
    post_id: int = Field(description="ID поста, который пользователь лайкнул")


class PostLikeRead(BaseModel):
    id: int
    user: UserRead
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
# ------------------------------------------