from datetime import timedelta
from uuid import uuid4
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import logging

from app.entities.user import User
from app.auth.schemas import RegisterUserRequest, Token, UserResponse
from app.auth.security import (
    get_password_hash,
    verify_password,
    create_access_token,
)
from app.exceptions import AuthenticationError
from fastapi import HTTPException, status
from app.config import settings


def register_user(db: Session, register_request: RegisterUserRequest) -> UserResponse:
    existing_user = db.query(User).filter(
        User.email == register_request.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    try:
        new_user = User(
            id=uuid4(),
            email=register_request.email,
            first_name=register_request.first_name,
            last_name=register_request.last_name,
            phone=register_request.phone,
            password_hash=get_password_hash(register_request.password),
            is_active=True
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        logging.info(
            f"✅ User registered successfully: {register_request.email}")

        return UserResponse.model_validate(new_user)

    except IntegrityError as e:
        db.rollback()
        logging.error(
            f"❌ Database integrity error during registration: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    except Exception as e:
        db.rollback()
        logging.error(f"❌ Failed to register user: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to register user"
        )


def authenticate_user(email: str, password: str, db: Session) -> User | None:
    user = db.query(User).filter(User.email == email).first()

    if not user:
        logging.warning(
            f"⚠️  Authentication failed: user not found for email {email}")
        return None

    if not user.is_active:
        logging.warning(
            f"⚠️  Authentication failed: user inactive for email {email}")
        return None

    if not verify_password(password, user.password_hash):
        logging.warning(
            f"⚠️  Authentication failed: invalid password for email {email}")
        return None

    logging.info(f"✅ User authenticated successfully: {email}")
    return user


def login_for_access_token(email: str, password: str, db: Session) -> Token:
    user = authenticate_user(email, password, db)

    if not user:
        raise AuthenticationError()

    access_token = create_access_token(
        email=user.email,
        user_id=user.id,
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return Token(access_token=access_token, token_type="bearer")
