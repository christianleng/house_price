from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict


class RegisterUserRequest(BaseModel):
    email: EmailStr
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)
    phone: str = Field(..., min_length=10, max_length=20)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: str | None = None
    email: str | None = None

    def get_uuid(self) -> UUID | None:
        if self.user_id:
            return UUID(self.user_id)
        return None


class UserResponse(BaseModel):
    id: UUID
    email: str
    first_name: str
    last_name: str
    phone: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
