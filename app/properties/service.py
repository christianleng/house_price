from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from app.entities.properties import Property
from app.entities.agent import Agent
from app.properties import schemas
import math
from fastapi import HTTPException, status
import logging
from uuid import UUID


def search_properties(
    db: Session, filters: schemas.PropertyFilterParams
) -> schemas.PaginatedPropertiesResponse:
    query = db.query(Property)

    if filters.city:
        query = query.filter(Property.city == filters.city)

    if filters.price_min:
        query = query.filter(Property.price >= filters.price_min)

    if filters.price_max:
        query = query.filter(Property.price <= filters.price_max)

    if filters.rooms_min:
        query = query.filter(Property.rooms >= filters.rooms_min)

    if filters.has_parking is not None:
        query = query.filter(Property.has_parking == filters.has_parking)

    if filters.has_garden is not None:
        query = query.filter(Property.has_garden == filters.has_garden)

    if filters.has_balcony is not None:
        query = query.filter(Property.has_balcony == filters.has_balcony)

    if filters.has_terrace is not None:
        query = query.filter(Property.has_terrace == filters.has_terrace)

    if filters.has_elevator is not None:
        query = query.filter(Property.has_elevator == filters.has_elevator)

    if filters.has_cave is not None:
        query = query.filter(Property.has_cave == filters.has_cave)

    if filters.property_type:
        query = query.filter(Property.property_type == filters.property_type)

    if filters.surface_min:
        query = query.filter(Property.surface_area >= filters.surface_min)

    if filters.bedrooms_min:
        query = query.filter(Property.bedrooms >= filters.bedrooms_min)

    total = query.count()

    sort_column = getattr(Property, filters.sort_by)

    if filters.sort_order == "asc":
        query = query.order_by(sort_column.asc())
    else:
        query = query.order_by(sort_column.desc())

    skip = (filters.page - 1) * filters.page_size

    query = query.offset(skip).limit(filters.page_size)

    properties = query.all()

    total_pages = math.ceil(total / filters.page_size)

    items = [
        schemas.PropertySummaryResponse.model_validate(prop) for prop in properties
    ]

    return schemas.PaginatedPropertiesResponse(
        items=items,
        total=total,
        page=filters.page,
        page_size=filters.page_size,
        total_pages=total_pages,
    )


def create_properties(
    property_data: schemas.CreatePropertyRequest, current_agent: UUID, db: Session
) -> schemas.PropertyResponse:
    property_exist = (
        db.query(Property).filter(Property.reference == property_data.reference).first()
    )
    if property_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Property with reference '{property_data.reference}' already exists",
        )

    try:
        new_property = Property(
            agent_id=current_agent,
            reference=property_data.reference,
            title=property_data.title,
            address=property_data.address,
            neighborhood=property_data.neighborhood,
            city=property_data.city,
            district=property_data.district,
            postal_code=property_data.postal_code,
            latitude=property_data.latitude,
            longitude=property_data.longitude,
            price=property_data.price,
            price_per_sqm=property_data.price_per_sqm,
            property_type=property_data.property_type,
            surface_area=property_data.surface_area,
            rooms=property_data.rooms,
            bedrooms=property_data.bedrooms,
            bathrooms=property_data.bathrooms,
            toilets=property_data.toilets,
            floors=property_data.floors,
            has_garden=property_data.has_garden,
            has_terrace=property_data.has_terrace,
            has_balcony=property_data.has_balcony,
            has_parking=property_data.has_parking,
            has_cave=property_data.has_cave,
            has_elevator=property_data.has_elevator,
            # has_pool=property_data.has_pool,
            # is_quiet=property_data.is_quiet,
            heating_type=property_data.heating_type,
            energy_rating=property_data.energy_rating,
            description=property_data.description,
            # is_active=property_data.is_active,
        )

        db.add(new_property)
        db.commit()
        db.refresh(new_property)

        logging.info(
            f"✅ Property created successfully: {new_property.reference} by agent {current_agent}"
        )

        return schemas.PropertyResponse.model_validate(new_property)
    except Exception as e:
        db.rollback()
        logging.error(f"❌ Failed to create property: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create property",
        )


def count_properties(db: Session, filters: schemas.PropertyFilterParams) -> int:
    query = db.query(Property)

    if filters.city:
        query = query.filter(Property.city == filters.city)
    if filters.postal_code:
        query = query.filter(Property.postal_code == filters.postal_code)
    if filters.price_min is not None:
        query = query.filter(Property.price >= filters.price_min)
    if filters.price_max is not None:
        query = query.filter(Property.price <= filters.price_max)
    if filters.rooms_min is not None:
        query = query.filter(Property.rooms >= filters.rooms_min)
    if filters.surface_min is not None:
        query = query.filter(Property.surface_area >= filters.surface_min)
    if filters.property_type:
        query = query.filter(Property.property_type == filters.property_type)

    if filters.has_parking is not None:
        query = query.filter(Property.has_parking == filters.has_parking)
    if filters.has_garden is not None:
        query = query.filter(Property.has_garden == filters.has_garden)
    if filters.has_balcony is not None:
        query = query.filter(Property.has_balcony == filters.has_balcony)
    if filters.has_elevator is not None:
        query = query.filter(Property.has_elevator == filters.has_elevator)

    return query.count()


def get_property_by_id(property_id: UUID, db: Session):
    property = db.query(Property).filter(Property.id == property_id).first()

    if not property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Property not found"
        )

    return schemas.PropertyResponse.model_validate(property)


def get_agent_properties(
    agent_id: UUID, filters: schemas.PropertyFilterParams, db: Session
) -> schemas.PaginatedPropertiesResponse:
    agent = db.query(Agent).filter(Agent.id == agent_id).first()

    if not agent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Agent not found"
        )

    query = db.query(Property).filter(Property.agent_id == agent_id)

    if filters.city:
        query = query.filter(Property.city == filters.city)

    if filters.price_min:
        query = query.filter(Property.price >= filters.price_min)

    if filters.price_max:
        query = query.filter(Property.price <= filters.price_max)

    if filters.property_type:
        query = query.filter(Property.property_type == filters.property_type)

    total = query.count()

    sort_column = getattr(Property, filters.sort_by)
    if filters.sort_order == "asc":
        query = query.order_by(sort_column.asc())
    else:
        query = query.order_by(sort_column.desc())

    skip = (filters.page - 1) * filters.page_size
    query = query.offset(skip).limit(filters.page_size)

    properties = query.all()

    total_pages = math.ceil(total / filters.page_size)

    items = [
        schemas.PropertySummaryResponse.model_validate(prop) for prop in properties
    ]

    return schemas.PaginatedPropertiesResponse(
        items=items,
        total=total,
        page=filters.page,
        page_size=filters.page_size,
        total_pages=total_pages,
        has_next=filters.page < total_pages,
        has_previous=filters.page > 1,
    )


def update_property(
    property_id: UUID,
    update_data: schemas.UpdatePropertyRequest,
    current_agent: UUID,
    db: Session,
):
    property_exist = db.query(Property).filter(Property.id == property_id).first()
    if not property_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Property not correct"
        )

    if property_exist.agent_id != current_agent:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not your property. You can only modify your own properties.",
        )

    update_dict = update_data.model_dump(exclude_unset=True)

    for field, value in update_dict.items():
        setattr(property_exist, field, value)

    try:
        db.commit()
        db.refresh(property_exist)

        logging.info(f"✅ Property updated: {property_exist.reference}")

        return schemas.PropertyResponse.model_validate(property_exist)
    except Exception as e:
        db.rollback()
        logging.error(f"❌ Failed to update property: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update property",
        )


def delete_property(
    property_id: UUID,
    current_agent: UUID,
    db: Session,
) -> None:
    property_to_delete = db.query(Property).filter(Property.id == property_id).filter()
    if not property_to_delete:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Property not correct"
        )

    if property_to_delete.agent_id != current_agent:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not your property. You can only delete your own properties.",
        )
    try:
        db.delete(property_to_delete)
        db.commit()

        logging.info(f"✅ Property deleted: {property_to_delete.reference}")

    except Exception as e:
        db.rollback()
        logging.error(f"❌ Failed to update property: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update property",
        )
