import pytest

from app.monitor import ping


@pytest.mark.asyncio
async def test_ping_200():
    status = await ping("https://httpstat.us/200")
    assert 200 == status


@pytest.mark.asyncio
async def test_ping_400():
    status = await ping("https://httpstat.us/400")
    assert 400 == status
