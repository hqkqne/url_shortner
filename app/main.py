import uvicorn
from fastapi import FastAPI
from db import lifespan
from router import router


app = FastAPI(lifespan= lifespan)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload= True)


