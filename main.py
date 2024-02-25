from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager

from create_tables import create_tables, drop_tables
from task_router import router as taskRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    await drop_tables()


# app = FastAPI(lifespan=lifespan)
app = FastAPI()
app.include_router(taskRouter)


@app.get("/")
async def get_start():
    return RedirectResponse("/tasks")


