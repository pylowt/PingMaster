import pytest

from app.monitor import ping


@pytest.mark.asyncio
async def test_ping():
    status = await ping()
    assert 200 == status
