from typing import Annotated, Union
from fastapi import APIRouter, Depends, Request, status
from fastapi.security import OAuth2PasswordRequestForm

from app.agents.dependencies import CurrentAgent
from app.auth import schemas, service
from app.auth.dependencies import CurrentTokenData, CurrentUser
from app.database.core import DbSession
from app.rate_limiting import limiter

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Create a new user account with email and password",
)
@limiter.limit("5/hour")
async def register_user(
    request: Request, db: DbSession, register_request: schemas.RegisterUserRequest
):
    return service.register_user(db, register_request)


@router.post(
    "/token",
    response_model=Union[schemas.TokenWithUser, schemas.TokenWithAgent],
    summary="Login for access token",
    description="""
    Endpoint de login unifié pour Users et Agents.
    
    - Cherche d'abord dans les Users
    - Si non trouvé, cherche dans les Agents
    - Retourne un token avec le rôle ('user' ou 'agent')
    
    Le token contient le rôle qui détermine les accès aux routes protégées.
    """,
)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: DbSession
):
    return service.login_for_access_token(
        email=form_data.username, password=form_data.password, db=db
    )


@router.get(
    "/me",
    response_model=Union[schemas.UserResponse, schemas.AgentResponse],
    summary="Get current authenticated entity",
    description="Returns the current user or agent based on the token",
)
async def get_me(token_data: CurrentTokenData, db: DbSession):
    from app.entities.user import User
    from app.entities.agent import Agent

    if token_data.is_user():
        user = db.query(User).filter(User.id == token_data.get_uuid()).first()
        if user:
            return schemas.UserResponse.model_validate(user)

    elif token_data.is_agent():
        agent = db.query(Agent).filter(Agent.id == token_data.get_uuid()).first()
        if agent:
            return schemas.AgentResponse.model_validate(agent)

    from fastapi import HTTPException

    raise HTTPException(status_code=404, detail="Entity not found")


@router.get(
    "/me/user",
    response_model=schemas.UserResponse,
    summary="Get current user (users only)",
    description="Get the currently authenticated user's information. Agents cannot access this.",
)
async def get_current_user_info(current_user: CurrentUser):
    return schemas.UserResponse.model_validate(current_user)


@router.get(
    "/me/agent",
    response_model=schemas.AgentResponse,
    summary="Get current agent (agents only)",
    description="Get the currently authenticated agent's information. Users cannot access this.",
)
async def get_current_agent_info(current_agent: CurrentAgent):
    return schemas.AgentResponse.model_validate(current_agent)
