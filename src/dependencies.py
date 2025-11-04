from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session

from fastapi import Depends


SessionDepends = Annotated[AsyncSession, Depends(get_session)]