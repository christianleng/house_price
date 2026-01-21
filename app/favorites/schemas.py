from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict
from uuid import UUID

from app.properties.schemas import PropertySummaryResponse


class FavoriteListResponse(BaseModel):
    items: List[PropertySummaryResponse]
    total: int

    model_config = ConfigDict(from_attributes=True)


class FavoriteResponse(BaseModel):
    id: UUID
    property_id: UUID
    user_id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
