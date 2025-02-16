"""
Models
"""

import uuid
from datetime import datetime, timezone
from enum import Enum

from sqlmodel import Field, SQLModel


class RoleEnum(str, Enum):
    """
    Enum class for role choices
    """

    ADMIN = "admin"
    USER = "user"


class User(SQLModel, table=True):
    """
    User model
    """

    __tablename__ = "users"
    user_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()), primary_key=True, nullable=False
    )
    username: str = Field(unique=True, index=True, nullable=False)
    email: str = Field(unique=True, index=True, nullable=False)
    first_name: str
    last_name: str
    password: str = Field(nullable=False, exclude=True)
    role: RoleEnum = Field(default=RoleEnum.USER, nullable=False)
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )

    def __repr__(self):
        return f"<User {self.username}>"
