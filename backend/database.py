from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine, AsyncEngine
from sqlalchemy.orm import declarative_base

URL_DATABASE: str = "postgresql+asyncpg://admin:admin@localhost:5433/habits_db"
engine: AsyncEngine = create_async_engine(URL_DATABASE, echo=True)
async_session: async_sessionmaker[AsyncSession | Any] = async_sessionmaker(bind=engine, expire_on_commit=False,
                                                                           class_=AsyncSession)

Base: declarative_base = declarative_base()
