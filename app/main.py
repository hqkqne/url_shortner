from fastapi import FastAPI, Depends
from app.db import lifespan
from schemas import *

app = FastAPI(lifespan= lifespan)

@app.post("/URL")
async def get_original_URL(Url: URLCreate,):
    return {"ok": True}
