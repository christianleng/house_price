from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict


class RegisterAgentRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100,
                      description="Nom complet de l'agent")
    agency_name: str = Field(..., min_length=2,
                             max_length=100, description="Nom de l'agence")
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=20)
    password: str = Field(..., min_length=8, max_length=100)
    rsac_number: str = Field(..., min_length=5,
                             max_length=50, description="Numéro RSAC")
    city: str = Field(..., min_length=2, max_length=100)

    @field_validator('rsac_number')
    @classmethod
    def validate_rsac(cls, v: str) -> str:
        # Exemple: RSAC doit commencer par des chiffres
        if not any(c.isdigit() for c in v):
            raise ValueError('RSAC number must contain at least one digit')
        return v.upper()  # Normalise en majuscules


class AgentResponse(BaseModel):
    id: UUID
    name: str
    agency_name: str
    email: str
    phone: str
    rsac_number: str
    city: str
    is_verified: bool
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AgentToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
    agent: AgentResponse


class AgentTokenData(BaseModel):
    agent_id: str | None = None
    email: str | None = None

    def get_uuid(self) -> UUID | None:
        if self.agent_id:
            return UUID(self.agent_id)
        return None


class UpdateAgentRequest(BaseModel):
    name: str | None = None
    agency_name: str | None = None
    phone: str | None = None
    city: str | None = None

    model_config = ConfigDict(from_attributes=True)
