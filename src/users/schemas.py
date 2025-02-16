"""
User schemas
"""

from enum import Enum

from pydantic import BaseModel, Field


class RoleEnum(str, Enum):
    """
    Enum class for role choices
    """

    ADMIN = "admin"
    USER = "user"


class SignupRequestSchema(BaseModel):
    """
    Signup request schema
    """

    username: str = Field(max_length=25)
    email: str = Field(max_length=40)
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    password: str = Field(min_length=8, max_length=20)

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "johndoe",
                "email": "johndoe1@co.com",
                "first_name": "John",
                "last_name": "Doe",
                "password": "testpass123",
            }
        }
    }


class SignupResponseSchema(BaseModel):
    """
    Signup response schema
    """

    username: str = Field(max_length=25)
    email: str = Field(max_length=40)
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    role: RoleEnum
    is_verified: bool
