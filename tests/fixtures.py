import pytest
import httpx
import pytest_asyncio

from src.app import app


@pytest_asyncio.fixture
async def httpx_client():
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://test"
        ) as client:
        yield client