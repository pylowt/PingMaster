import os
import httpx
import pytest

from app.monitor import ping

BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")


@pytest.mark.asyncio
async def test_ping_200():
    status = await ping(f"{BASE_URL}/ok")
    assert 200 == status


@pytest.mark.asyncio
async def test_ping_400():
    status = await ping(f"{BASE_URL}/bad")
    assert 400 == status


@pytest.mark.asyncio
async def test_timeout():
    with pytest.raises(httpx.TimeoutException):
        await ping(f"{BASE_URL}/timeout", timeout=0.2)
