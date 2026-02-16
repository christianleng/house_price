import math
import logging
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from uuid import UUID
from fastapi import HTTPException, status
from app.entities.properties import Property
from app.entities.agent import Agent
from app.admin.properties import schemas
from app.properties import schemas as property_schemas


def get_admin_properties(
    db: Session,
    search: str | None,
    transaction_type: str | None,
    status_filter: str | None,
    city: str | None,
    energy_rating: str | None,
    price_min: int | None,
    price_max: int | None,
    page: int,
    limit: int,
) -> schemas.AdminPropertiesResponse:

    query = db.query(Property)

    if search:
        pattern = f"%{search.lower()}%"
        query = query.filter(
            or_(
                Property.title.ilike(pattern),
                Property.reference.ilike(pattern),
            )
        )

    if transaction_type:
        query = query.filter(Property.transaction_type == transaction_type)

    if status_filter == "active":
        query = query.filter(Property.is_active == True)
    elif status_filter == "inactive":
        query = query.filter(Property.is_active == False)

    if city:
        query = query.filter(Property.city.ilike(f"%{city}%"))

    if energy_rating:
        query = query.filter(Property.energy_rating == energy_rating)

    if price_min is not None:
        query = query.filter(
            and_(
                Property.transaction_type == "sale",
                Property.price >= price_min,
            )
            | and_(
                Property.transaction_type == "rent",
                Property.rent_price_monthly >= price_min,
            )
        )

    if price_max is not None:
        query = query.filter(
            and_(
                Property.transaction_type == "sale",
                Property.price <= price_max,
            )
            | and_(
                Property.transaction_type == "rent",
                Property.rent_price_monthly <= price_max,
            )
        )

    total = query.count()
    offset = (page - 1) * limit
    properties = (
        query.order_by(Property.created_at.desc()).offset(offset).limit(limit).all()
    )

    return schemas.AdminPropertiesResponse(
        items=[schemas.AdminPropertyItem.model_validate(prop) for prop in properties],
        total=total,
        page=page,
        limit=limit,
        pages=math.ceil(total / limit) if total > 0 else 1,
    )


def get_property_by_id(
    property_id: UUID,
    db: Session,
) -> property_schemas.PropertyResponse:
    prop = db.query(Property).filter(Property.id == property_id).first()
    if not prop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found",
        )
    return property_schemas.PropertyResponse.model_validate(prop)


def update_property(
    property_id: UUID,
    update_data: property_schemas.UpdatePropertyRequest,
    db: Session,
) -> property_schemas.PropertyResponse:
    prop = db.query(Property).filter(Property.id == property_id).first()
    if not prop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found",
        )

    update_dict = update_data.model_dump(exclude_unset=True)
    for field, value in update_dict.items():
        setattr(prop, field, value)

    try:
        db.commit()
        db.refresh(prop)
        logging.info(f"✅ Property updated by admin: {prop.reference}")
        return property_schemas.PropertyResponse.model_validate(prop)
    except Exception as e:
        db.rollback()
        logging.error(f"❌ Failed to update property: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update property",
        )


def delete_property(property_id: UUID, db: Session) -> None:
    prop = db.query(Property).filter(Property.id == property_id).first()
    if not prop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found",
        )
    try:
        db.delete(prop)
        db.commit()
        logging.info(f"✅ Property deleted by admin: {prop.reference}")
    except Exception as e:
        db.rollback()
        logging.error(f"❌ Failed to delete property: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete property",
        )


def get_agent_properties(
    agent_id: UUID,
    db: Session,
    page: int = 1,
    limit: int = 20,
) -> schemas.AdminPropertiesResponse:
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found",
        )

    query = db.query(Property).filter(Property.agent_id == agent_id)
    total = query.count()
    properties = (
        query.order_by(Property.created_at.desc())
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    return schemas.AdminPropertiesResponse(
        items=[schemas.AdminPropertyItem.model_validate(prop) for prop in properties],
        total=total,
        page=page,
        limit=limit,
        pages=math.ceil(total / limit) if total > 0 else 1,
    )
