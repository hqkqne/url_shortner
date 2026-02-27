import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import engine
from models import Base
from routers import router

# async def create_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
# async def drop_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Base is ready")
    yield
    print('Get off')
    await engine.dispose()

app = FastAPI(lifespan= lifespan)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload= True)


