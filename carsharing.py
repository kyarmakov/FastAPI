import uvicorn
from fastapi import *
from sqlmodel import SQLModel

from db import engine
from routers import cars, web, auth

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(title="Car Sharing", lifespan=lifespan)
app.include_router(cars.router)
app.include_router(web.router)
app.include_router(auth.router)


@app.middleware('http')
async def add_cars_cookie(request: Request, call_next):
    response = await call_next(request)
    response.set_cookie(key='cars_cookie', value='you visited the carsharing app')
    return response


if __name__ == '__main__':
    uvicorn.run('carsharing:app', reload=True)
