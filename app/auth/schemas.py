from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from enum import Enum

from app.agents.schemas import AgentResponse


class UserRole(str, Enum):
    USER = "user"
    AGENT = "agent"


class RegisterUserRequest(BaseModel):
    email: EmailStr
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)
    phone: str = Field(..., min_length=10, max_length=20)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: str
    email: str | None = None
    role: UserRole

    def get_uuid(self) -> UUID:
        return UUID(self.user_id)

    def is_agent(self) -> bool:
        return self.role == UserRole.AGENT

    def is_user(self) -> bool:
        return self.role == UserRole.USER


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: UserRole


class TokenWithUser(Token):
    user: "UserResponse"


class TokenWithAgent(Token):
    agent: "AgentResponse"


class UserResponse(BaseModel):
    id: UUID
    email: str
    first_name: str
    last_name: str
    phone: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
