import asyncio

from fastapi import FastAPI
from fastapi import status
from fastapi.responses import Response

app = FastAPI()


@app.get("/ok")
async def ok():
    return Response(status_code=status.HTTP_200_OK)


@app.get("/bad")
async def bad():
    return Response(status_code=status.HTTP_400_BAD_REQUEST)


@app.get("/timeout")
async def timeout():
    # Ping function must be invoked with a timeout < 0.5s
    await asyncio.sleep(0.5)
    return Response(status_code=status.HTTP_400_BAD_REQUEST)
