from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table, drop_table

from routers import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_table()
    print("drop database")
    await create_table()
    print("Creating  models")
    yield
    print("starting to drop")


app = FastAPI(lifespan=lifespan)
app.include_router(router)




