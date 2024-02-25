from sqlalchemy import select

from database import async_session
from dtos import STaskAdd, STask
from models import Task


class TaskRepository:
    @classmethod
    async def add_one(cls, task: STaskAdd):
        async with async_session() as session:
            task_orm = Task(**task.model_dump())
            session.add(task_orm)
            await session.flush()
            task_id = task_orm.id
            await session.commit()
            return task_id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with async_session() as session:
            res = await session.execute(select(Task))
            res = res.scalars().all()
            tasks = [STask.model_validate(task, from_attributes=True) for task in res]
            return tasks
