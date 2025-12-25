from sqlalchemy import Column, String, Table, ForeignKey, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database.core import Base
from app.entities.enum import FeatureCategory


# Table de liaison (Many-to-Many)
property_features = Table(
    "property_features",
    Base.metadata,
    Column("property_id", UUID(as_uuid=True),
           ForeignKey("properties.id"), primary_key=True),
    Column("feature_id", UUID(as_uuid=True),
           ForeignKey("features.id"), primary_key=True)
)


class Feature(Base):
    __tablename__ = "features"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)
    category = Column(SQLEnum(FeatureCategory), nullable=True)
    icon = Column(String, nullable=True)

    properties = relationship(
        "Property", secondary=property_features, back_populates="features")
