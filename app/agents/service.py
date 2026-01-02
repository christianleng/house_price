from datetime import timedelta
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import logging

from app.entities.agent import Agent
from app.agents.schemas import (
    RegisterAgentRequest,
    AgentResponse,
    AgentToken,
    UpdateAgentRequest,
)
from app.auth.security import get_password_hash, verify_password, create_access_token
from app.config import settings
from fastapi import HTTPException, status


def register_agent(
    db: Session, register_request: RegisterAgentRequest
) -> AgentResponse:
    existing_agent = (
        db.query(Agent).filter(Agent.email == register_request.email).first()
    )
    if existing_agent:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    existing_rsac = (
        db.query(Agent)
        .filter(Agent.rsac_number == register_request.rsac_number)
        .first()
    )
    if existing_rsac:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="RSAC number already registered",
        )

    try:
        new_agent = Agent(
            id=uuid4(),
            name=register_request.name,
            agency_name=register_request.agency_name,
            email=register_request.email,
            phone=register_request.phone,
            password_hash=get_password_hash(register_request.password),
            rsac_number=register_request.rsac_number,
            city=register_request.city,
            is_verified=False,
            is_active=True,
        )

        db.add(new_agent)
        db.commit()
        db.refresh(new_agent)

        logging.info(f"✅ Agent registered successfully: {register_request.email}")

        return AgentResponse.model_validate(new_agent)

    except IntegrityError as e:
        db.rollback()
        logging.error(
            f"❌ Database integrity error during agent registration: {str(e)}"
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Agent registration failed - duplicate data",
        )

    except Exception as e:
        db.rollback()
        logging.error(f"❌ Failed to register agent: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to register agent",
        )


def authenticate_agent(email: str, password: str, db: Session) -> Agent | None:
    agent = db.query(Agent).filter(Agent.email == email).first()

    if not agent:
        logging.warning(f"⚠️  Agent not found: {email}")
        return None

    if not agent.is_active:
        logging.warning(f"⚠️  Agent inactive: {email}")
        return None

    if not verify_password(password, agent.password_hash):
        logging.warning(f"⚠️  Invalid password for agent: {email}")
        return None

    logging.info(f"✅ Agent authenticated: {email}")
    return agent


def login_agent_for_access_token(email: str, password: str, db: Session) -> AgentToken:
    agent = authenticate_agent(email, password, db)

    if not agent:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not agent.is_verified:
        logging.warning(f"⚠️  Unverified agent logged in: {email}")

    access_token = create_access_token(
        email=agent.email,
        user_id=agent.id,
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return AgentToken(
        access_token=access_token,
        token_type="bearer",
        agent=AgentResponse.model_validate(agent),
    )


def get_agent_by_id(agent_id: UUID, db: Session) -> Agent:
    agent = db.query(Agent).filter(Agent.id == agent_id).first()

    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Agent not found"
        )

    return agent


def update_agent(
    agent_id: UUID, update_data: UpdateAgentRequest, db: Session
) -> AgentResponse:
    agent = get_agent_by_id(agent_id, db)

    update_dict = update_data.model_dump(exclude_unset=True)

    for field, value in update_dict.items():
        setattr(agent, field, value)

    try:
        db.commit()
        db.refresh(agent)
        logging.info(f"✅ Agent updated: {agent.email}")
        return AgentResponse.model_validate(agent)

    except Exception as e:
        db.rollback()
        logging.error(f"❌ Failed to update agent: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update agent",
        )


def verify_agent(agent_id: UUID, db: Session) -> AgentResponse:
    agent = get_agent_by_id(agent_id, db)
    agent.is_verified = True

    db.commit()
    db.refresh(agent)

    logging.info(f"✅ Agent verified: {agent.email}")
    return AgentResponse.model_validate(agent)
