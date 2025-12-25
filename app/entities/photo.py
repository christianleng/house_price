from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from app.database.core import Base


class Photo(Base):
    __tablename__ = "photos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    property_id = Column(UUID(as_uuid=True), ForeignKey(
        'properties.id'), nullable=False)
    url = Column(String, nullable=False)
    is_primary = Column(Boolean, default=False)
    display_order = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    property = relationship("Property", back_populates="photos")
