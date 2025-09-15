from fastapi import APIRouter

from src.auth.router import router as auth_router
from src.posts.router import router as posts_router
from src.comments.router import router as comments_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(posts_router, prefix="/posts", tags=["Posts"])
router.include_router(comments_router, prefix="/comments", tags=["Comments"])
