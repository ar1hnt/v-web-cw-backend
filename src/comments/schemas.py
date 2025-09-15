from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from datetime import datetime

from src.auth.schemas import UserRead


# COMMENT ----------------------------------
class CommentBase(BaseModel):
    text: str = Field(min_length=1)
    parent_id: Optional[int] = Field(default=None, description="ID родительского комментария")


class CommentCreate(CommentBase):
    post_id: int = Field(description="ID поста, к которому относится комментарий")


class CommentRead(CommentBase):
    id: int
    post_id: int
    author: UserRead
    created_at: datetime
    updated_at: Optional[datetime]
    replies: List[CommentRead] = []
    likes_count: int = 0

    model_config = ConfigDict(from_attributes=True)


class CommentUpdate(BaseModel):
    text: Optional[str] = Field(min_length=1)
# ------------------------------------------


# COMMENT LIKES ----------------------------
class CommentLikeCreate(BaseModel):
    comment_id: int = Field(description="ID комментария, который пользователь лайкнул")


class CommentLikeRead(BaseModel):
    id: int
    user: UserRead
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
# ------------------------------------------