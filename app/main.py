from fastapi import FastAPI, Depends
from app.db import lifespan

app = FastAPI(lifespan= lifespan)

