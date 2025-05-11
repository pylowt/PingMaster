import httpx
import yaml

TIMEOUT = 5


def load_config():
    with open("app/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config


async def ping(url: str, timeout=TIMEOUT) -> int:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, timeout=timeout)
        return resp.status_code


async def schedule_checks():
    # Aim: create a scheduler that reads the urls to check and interval from the config file
    # use asyncio to create a task that runs a ping for each url
    # Steps:
    # 1. Read URLs from config
    config = load_config()
    urls = config.get("urls", [])
    # 2. Read interval from config
    interval = config.get("interval_seconds", 60)

    # 3. The next step is more complex. Need to execute these as async coroutines to ensure multiple outbound
    #    http requests can be made simultaneously. How do I gather these url's into a list for asyncio to execute them?
    # Schedule three calls *concurrently*:
    # from stackoverflow:
    # await asyncio.gather(
    #     factorial("A", 2),
    #     factorial("B", 3),
    #     factorial("C", 4),
    # )

    pass
