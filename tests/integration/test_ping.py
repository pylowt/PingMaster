import os
import subprocess
import time

import httpx
import pytest

from app.monitor import ping

BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")


@pytest.fixture(scope="class")
def ci_server():
    # Setup a fastapi test server with endpoints returning various status codes
    proc = subprocess.Popen(
        ["poetry", "run", "uvicorn", "tests.ci_server:app", "--port", "8000"]
    )
    print("running setup")
    # Crude method for ensuring the server is ready.
    # TODO: investigate a method to probe the server to confirm startup negating the time.sleep method
    time.sleep(1)
    yield
    print("running teardown")
    proc.terminate()


@pytest.mark.usefixtures("ci_server")
class TestPingEndpoints:

    @pytest.mark.asyncio
    async def test_ping_200(self):
        status = await ping(f"{BASE_URL}/ok")
        assert 200 == status

    @pytest.mark.asyncio
    async def test_ping_400(self):
        status = await ping(f"{BASE_URL}/bad")
        assert 400 == status

    @pytest.mark.asyncio
    async def test_timeout(self):
        with pytest.raises(httpx.TimeoutException):
            await ping(f"{BASE_URL}/timeout", timeout=0.2)
