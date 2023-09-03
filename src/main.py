import os
import asyncio
from fastapi import FastAPI

app = FastAPI()
threshold = os.getenv('THRESHOLD', 1024)
counter = 0
lock = asyncio.Lock()


@app.get("/increment")
async def increment() -> dict[str, bool]:
    global counter
    with lock:
        counter += 1
        if counter == threshold:
            counter = 0
            return {'calculate': True}
    return {'calculate': False}
