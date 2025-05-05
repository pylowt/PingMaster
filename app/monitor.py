import httpx

TIMEOUT = 5


async def ping(url: str, timeout=TIMEOUT) -> int:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, timeout=timeout)
        return resp.status_code
