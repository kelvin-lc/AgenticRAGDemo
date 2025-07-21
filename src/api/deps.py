from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.config import settings

engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URI,
    echo=True,
    future=True,
    pool_size=200,
    max_overflow=100,
    pool_timeout=65,
    pool_recycle=3600 * 4,
)

async_session_maker = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


@asynccontextmanager
async def session_maker() -> AsyncSession:
    session = async_session_maker()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()


async def get_session():
    async with session_maker() as session:
        yield session
