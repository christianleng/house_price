from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional


class AdminPropertyItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    reference: Optional[str]
    title: str
    city: str
    postal_code: str
    transaction_type: str
    property_type: str
    price: Optional[int]
    price_per_sqm: Optional[int] = None

    rent_price_monthly: Optional[int]
    surface_area: int
    rooms: int
    energy_rating: str
    is_active: bool
    photos_count: int
    views_count: int
    created_at: datetime
    updated_at: datetime
    thumbnail_url: Optional[str] = None


class AdminPropertiesResponse(BaseModel):
    items: list[AdminPropertyItem]
    total: int
    page: int
    limit: int
    pages: int
