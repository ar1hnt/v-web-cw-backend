from typing import Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session

from fastapi import APIRouter, Depends


router = APIRouter()

SessionDepends = Annotated[AsyncSession, Depends(get_session)]