from typing import Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from src.dependencies import SessionDepends
from src.posts.schemas import PostRead
from src.posts.models import Post

from fastapi import APIRouter, Depends


router = APIRouter()


@router.get(path="/all", summary="Получение всех постов", response_model=list[PostRead])
async def get_all_posts(session: SessionDepends):
    query = await session.execute(select(Post))
    return query.scalars().all()