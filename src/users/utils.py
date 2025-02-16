"""
Password hashing library
"""

from passlib.hash import bcrypt


def generate_password_hash(password: str) -> str:
    """
    Generate password hash
    """

    return bcrypt.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password
    """

    return bcrypt.verify(plain_password, hashed_password)
