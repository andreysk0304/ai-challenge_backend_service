from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.utils.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, pool_size=200)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session


async def create_db():
    from app.database.base import Base
    from app.database import models
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)