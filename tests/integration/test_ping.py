import os
import subprocess
import time
import httpx
import pytest

from app.monitor import ping

BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")


@pytest.fixture(scope="class")
def ci_server():
    # Setup
    # Set up a fastapi test server with endpoints returning various status codes
    proc = subprocess.Popen(
        ["poetry", "run", "uvicorn", "tests.ci_server:app", "--port", "8000"]
    )

    def wait_for_server(url: str, timeout: int = 5):
        start = time.time()
        while time.time() - start < timeout:
            try:
                response = httpx.get(url)
                if response.status_code == 200:
                    return True
            except httpx.RequestError:
                pass
            time.sleep(0.5)
        return False

    if not wait_for_server(f"{BASE_URL}/healthcheck"):
        # Ensure the subprocess is terminated as it has timed out, first try gracefully
        proc.terminate()
        try:
            # Wait to see if it has actually terminated in case it is hanging
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            # Force kill if it did not terminate
            proc.kill()
        raise TimeoutError("Server did not become ready within the timeout period")
    yield
    # Teardown
    proc.terminate()


@pytest.mark.usefixtures("ci_server")
class TestPingEndpoints:

    @pytest.mark.asyncio
    async def test_ping_200(self):
        status = await ping(f"{BASE_URL}/ok")
        assert status == 200

    @pytest.mark.asyncio
    async def test_ping_400(self):
        status = await ping(f"{BASE_URL}/bad")
        assert status == 400

    @pytest.mark.asyncio
    async def test_timeout(self):
        with pytest.raises(httpx.TimeoutException):
            await ping(f"{BASE_URL}/timeout", timeout=0.2)
