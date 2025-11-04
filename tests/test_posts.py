import pytest

from tests.fixtures import httpx_client


@pytest.mark.asyncio
async def test__get_all_posts(httpx_client):
    response = await httpx_client.get("/posts/all")
    assert response.status_code == 200