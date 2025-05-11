from unittest.mock import AsyncMock

import httpx
import pytest

from app.monitor import ping


@pytest.mark.asyncio
async def test_ping(monkeypatch):
    mocked_get = AsyncMock()
    mocked_get.return_value.status_code = 200
    monkeypatch.setattr(httpx.AsyncClient, "get", mocked_get)

    url = "http://random.url"
    status = await ping(url, timeout=5)
    mocked_get.assert_awaited_once_with(url, timeout=5)
    assert status == 200


@pytest.mark.asyncio
async def test_ping_timeout(monkeypatch):
    mocked_get = AsyncMock(side_effect=httpx.TimeoutException("Timeout"))
    mocked_get.return_value.status_code = 200
    monkeypatch.setattr(httpx.AsyncClient, "get", mocked_get)

    url = "http://random.url"
    with pytest.raises(httpx.TimeoutException):
        await ping(url, timeout=5)
    mocked_get.assert_awaited_once_with(url, timeout=5)
