"""
Database connection module
"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src import EnvConfig


# Create the async engine with configurable SQL logging
def create_engine() -> AsyncEngine:
    """
    Creates and returns an async engine.
    """
    return create_async_engine(
        url=EnvConfig.DATABASE_URL,
        echo=True,  # Toggle logging based on environment
        pool_size=10,  # Set a pool size for better performance
        max_overflow=20,  # Allow additional connections
    )


# Initialize engine and session factory
async_engine: AsyncEngine = create_engine()
async_session_factory = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Provides an async SQLAlchemy session.

    Example:
        async with get_session() as session:
            result = await session.execute(...)
    """
    async with async_session_factory() as session:
        yield session


async def shutdown_engine():
    """
    Properly shuts down the async engine to release resources.
    """
    await async_engine.dispose()
