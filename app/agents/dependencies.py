from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.core import get_db
from app.auth.dependencies import get_current_user_from_token
from app.auth.schemas import TokenData
from app.entities.agent import Agent


def get_current_agent(
    token_data: Annotated[TokenData, Depends(get_current_user_from_token)],
    db: Annotated[Session, Depends(get_db)]
) -> Agent:
    agent = db.query(Agent).filter(Agent.id == token_data.get_uuid()).first()

    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )

    if not agent.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive agent"
        )

    return agent


def get_current_verified_agent(
    current_agent: Annotated[Agent, Depends(get_current_agent)]
) -> Agent:
    if not current_agent.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Agent not verified. Please contact support."
        )

    return current_agent


CurrentAgent = Annotated[Agent, Depends(get_current_agent)]
CurrentVerifiedAgent = Annotated[Agent, Depends(get_current_verified_agent)]
