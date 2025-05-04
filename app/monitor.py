import httpx


async def ping(url: str) -> int:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        return resp.status_code
