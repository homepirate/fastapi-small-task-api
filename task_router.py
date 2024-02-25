from typing import Annotated

from fastapi import APIRouter, Depends

from dtos import STaskAdd, STask, STaskId
from repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/add")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"data": "ok", "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    res = await TaskRepository.get_all()
    return res
