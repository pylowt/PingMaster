import asyncio

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
    """
    Schedules periodic checks by loading configuration data, retrieving URLs and
    intervals; executes an async task to perform these checks.
    """
    config = load_config()
    urls = config.get("urls", [])
    interval = config.get("interval_seconds", 60)
    asyncio.create_task(runner(urls, interval))

async def runner(urls: list[str], interval: int = 60):
    """
    Executes periodic asynchronous checks for a list of URLs at specified intervals.

    This function takes a list of URLs and pings each one asynchronously. The
    interval between each set of pings can be specified as a parameter. If an
    exception occurs during the URL checks, the exception is logged to standard
    output and then re-raised. The function runs indefinitely until manually
    stopped, or an unhandled exception halts execution.

    :param urls: A list of URLs to check.
    :param interval: The time interval, in seconds, between consecutive checks.
                     Defaults to 60 seconds.
    :return: None
    """
    while True:
        try:
            await asyncio.gather(*[ping(url) for url in urls])
        except Exception as e:
            print(f"Error during URL checks: {e}")
            raise e
        await asyncio.sleep(interval)
