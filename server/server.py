from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncio

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, Kubernetes!"}

@app.get("/async-example")
async def async_example():
    await asyncio.sleep(1)
    return {"message": "This is an async response!"}