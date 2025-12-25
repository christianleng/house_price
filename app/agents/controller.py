from typing import Annotated
from fastapi import APIRouter, Depends, Request, status
from fastapi.security import OAuth2PasswordRequestForm

from app.agents import schemas, service
from app.agents.dependencies import CurrentAgent, CurrentVerifiedAgent
from app.database.core import DbSession
from app.rate_limiting import limiter

router = APIRouter(
    prefix='/agents',
    tags=['Agents']
)


@router.post(
    "/register",
    response_model=schemas.AgentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new agent",
    description="Create a new real estate agent account"
)
@limiter.limit("3/hour")
async def register_agent(
    request: Request,
    db: DbSession,
    register_request: schemas.RegisterAgentRequest
):
    return service.register_agent(db, register_request)


@router.post(
    "/token",
    response_model=schemas.AgentToken,
    summary="Login for access token",
    description="Authenticate an agent and receive a JWT access token"
)
async def login_agent_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: DbSession
):
    return service.login_agent_for_access_token(
        email=form_data.username,
        password=form_data.password,
        db=db
    )


@router.get(
    "/me",
    response_model=schemas.AgentResponse,
    summary="Get current agent",
    description="Get the currently authenticated agent's information"
)
async def get_current_agent_info(current_agent: CurrentAgent):
    return schemas.AgentResponse.model_validate(current_agent)


@router.patch(
    "/me",
    response_model=schemas.AgentResponse,
    summary="Update current agent",
    description="Update the authenticated agent's information"
)
async def update_current_agent(
    update_data: schemas.UpdateAgentRequest,
    current_agent: CurrentAgent,
    db: DbSession
):
    return service.update_agent(current_agent.id, update_data, db)


@router.get(
    "/verified-only",
    response_model=schemas.AgentResponse,
    summary="Verified agents only",
    description="Endpoint accessible only by verified agents"
)
async def verified_agents_only(current_agent: CurrentVerifiedAgent):
    return schemas.AgentResponse.model_validate(current_agent)
