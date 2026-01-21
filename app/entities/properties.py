from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
    DateTime,
    ForeignKey,
    Float,
    Enum as SQLEnum,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database.core import Base
from app.entities.enum import PropertyType, EnergyRating, HeatingType, TransactionType
from app.entities.feature import property_features
from datetime import datetime, timezone


class Property(Base):
    __tablename__ = "properties"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_id = Column(UUID(as_uuid=True), ForeignKey("agents.id"), nullable=False)
    reference = Column(String, nullable=True)

    title = Column(String, nullable=False)
    address = Column(String, nullable=True)
    neighborhood = Column(String, nullable=True)
    city = Column(String, nullable=False)
    district = Column(String, nullable=True)
    postal_code = Column(String, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    price = Column(Integer, nullable=False)
    price_per_sqm = Column(Integer, nullable=False)

    property_type = Column(
        SQLEnum(
            PropertyType, values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False,
    )
    surface_area = Column(Integer, nullable=False)
    rooms = Column(Integer, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=True)
    toilets = Column(Integer, nullable=True)
    floors = Column(Integer, nullable=True)

    has_garden = Column(Boolean, default=False)
    has_terrace = Column(Boolean, default=False)
    has_balcony = Column(Boolean, default=False)
    has_parking = Column(Boolean, default=False)
    has_cave = Column(Boolean, default=False)
    has_elevator = Column(Boolean, default=False)
    has_pool = Column(Boolean, default=False)
    is_quiet = Column(Boolean, default=False)

    floor_number = Column(Integer, nullable=True)
    parking_spaces = Column(Integer, default=0)
    construction_year = Column(Integer, nullable=True)
    available_from = Column(DateTime, nullable=True)
    is_furnished = Column(Boolean, default=False)

    heating_type = Column(
        SQLEnum(
            HeatingType, values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False,
    )
    energy_rating = Column(
        SQLEnum(
            EnergyRating, values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False,
    )

    description = Column(String, nullable=False)
    photos_count = Column(Integer, nullable=False, default=0)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    is_active = Column(Boolean, default=True)
    views_count = Column(Integer, nullable=False, default=0)

    transaction_type = Column(
        SQLEnum(
            TransactionType,
            values_callable=lambda enum_cls: [e.value for e in enum_cls],
        ),
        nullable=False,
        index=True,
    )

    rent_price_monthly = Column(Integer, nullable=True)
    charges_included = Column(Boolean, default=False)
    deposit = Column(Integer, nullable=True)

    agent = relationship("Agent", back_populates="properties")
    features = relationship(
        "Feature", secondary=property_features, back_populates="properties"
    )
    favorited_by = relationship(
        "Favorite", back_populates="property", cascade="all, delete-orphan"
    )
    photos = relationship(
        "Photo", back_populates="property", cascade="all, delete-orphan"
    )

    @property
    def thumbnail_url(self) -> str | None:
        if not self.photos:
            return None
        primary_photo = next((p for p in self.photos if p.is_primary), self.photos[0])
        return primary_photo.url_thumbnail
