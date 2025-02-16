"""
Users routes
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.utils import get_session
from src.users.schemas import SignupRequestSchema, SignupResponseSchema
from src.users.services import UserService

users_router = APIRouter()


def get_user_service(session: AsyncSession = Depends(get_session)) -> UserService:
    """
    Get the user service.

    Args:
    session (Session, optional): Database session dependency.
    Defaults to Depends(get_session).

    Returns:
    UserService: Instance of UserService.
    """
    return UserService(session)


@users_router.post("/signup", response_model=SignupResponseSchema)
async def signup(
    user_data: SignupRequestSchema,
    user_service: UserService = Depends(get_user_service),
):
    """
    Signup route
    """

    email = user_data.email

    user_exists = await user_service.user_exists(email)
    if user_exists:
        return {"message": "User already exists"}

    new_user = await user_service.create_user(user_data)

    return new_user


# @users_router.post("/login")
# async def login():
#     """
#     Login route
#     """

#     return {"message": "Hello from login!"}
