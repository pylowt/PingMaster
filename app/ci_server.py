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
