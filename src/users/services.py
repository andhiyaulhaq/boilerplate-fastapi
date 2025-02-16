"""
User service module
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from db.models import User
from src.users.schemas import SignupRequestSchema
from src.users.utils import generate_password_hash


class UserService:
    """
    User service class
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_email(self, email: str) -> User | None:
        """
        Get a user by email
        """
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        user = result.first()
        return user

    async def user_exists(self, email: str) -> bool:
        """
        Check if a user exists
        """

        user = await self.get_user_by_email(email)

        return user is not None

    async def create_user(self, user: SignupRequestSchema) -> User:
        """
        Create a new user
        """
        user.password = generate_password_hash(user.password)
        new_user = User(**user.model_dump())
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user
