import asyncio

from database import async_engine, Base
from models import *


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def main():
    await create_tables()


if __name__ == '__main__':
    asyncio.run(main())
