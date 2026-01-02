import hashlib
from datetime import timedelta, datetime, timezone
from uuid import UUID
from passlib.context import CryptContext
import jwt
from jwt import PyJWTError
import logging

from enum import Enum

from app.config import settings

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserRole(str, Enum):
    USER = "user"
    AGENT = "agent"


def get_password_hash(password: str) -> str:
    sha256_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return bcrypt_context.hash(sha256_hash)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    sha256_hash = hashlib.sha256(plain_password.encode("utf-8")).hexdigest()
    return bcrypt_context.verify(sha256_hash, hashed_password)


def create_access_token(
    email: str, user_id: UUID, role: UserRole, expires_delta: timedelta | None = None
) -> str:
    if expires_delta is None:
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    encode = {
        "sub": email,
        "id": str(user_id),
        "role": role.value,
        "exp": datetime.now(timezone.utc) + expires_delta,
    }

    return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        user_id: str = payload.get("id")
        email: str = payload.get("sub")
        role: str = payload.get("role")

        if user_id is None:
            raise PyJWTError("Token payload missing user_id")

        if role is None:
            raise PyJWTError("Token payload missing role")

        return {"user_id": user_id, "email": email, "role": role}

    except PyJWTError as e:
        logging.warning(f"Token verification failed: {str(e)}")
        raise
