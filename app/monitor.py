import httpx

TIMEOUT = 5


def load_config():
    pass


async def ping(url: str, timeout=TIMEOUT) -> int:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, timeout=timeout)
        return resp.status_code


async def schedule_checks():
    load_config()
    # Aim: create a scheduler that reads the urls to check and interval from the config file
    # use asyncio to create a task that runs a ping for each url
    # Steps:
    # 1. Read URLs from config
    # 2. Read interval from config
    # 3. The next step is more complex. Need to execute these as async coroutines to ensure multiple outbound
    #    http requests can be made simultaneously. How do I gather these url's into a list for asyncio to execute them?
    pass
