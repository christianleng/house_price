from typing import Annotated
from fastapi import APIRouter, Depends, Request, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth import schemas, service
from app.auth.dependencies import CurrentUser
from app.database.core import DbSession
from app.rate_limiting import limiter

router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)


@router.post(
    "/register",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Create a new user account with email and password"
)
@limiter.limit("5/hour")
async def register_user(
    request: Request,
    db: DbSession,
    register_request: schemas.RegisterUserRequest
):
    return service.register_user(db, register_request)


@router.post(
    "/token",
    response_model=schemas.Token,
    summary="Login for access token",
    description="Authenticate and receive a JWT access token"
)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: DbSession
):
    return service.login_for_access_token(
        email=form_data.username,
        password=form_data.password,
        db=db
    )


@router.get(
    "/me",
    response_model=schemas.UserResponse,
    summary="Get current user",
    description="Get the currently authenticated user's information"
)
async def get_current_user(current_user: CurrentUser):
    return schemas.UserResponse.model_validate(current_user)
