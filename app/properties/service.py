from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_, or_
from app.entities.enum import TransactionType
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
    query = db.query(Property).options(joinedload(Property.photos))

    if filters.city:
        query = query.filter(Property.city.ilike(f"%{filters.city}%"))

    if filters.district:
        query = query.filter(Property.district == filters.district)

    if filters.postal_code:
        query = query.filter(Property.postal_code == filters.postal_code)

    if filters.transaction_type:
        query = query.filter(Property.transaction_type == filters.transaction_type)

    if filters.transaction_type == "sale":
        if filters.price_min is not None:
            query = query.filter(Property.price >= filters.price_min)
        if filters.price_max is not None:
            query = query.filter(Property.price <= filters.price_max)
    elif filters.transaction_type == "rent":
        if filters.rent_price_min is not None:
            query = query.filter(Property.rent_price_monthly >= filters.rent_price_min)
        if filters.rent_price_max is not None:
            query = query.filter(Property.rent_price_monthly <= filters.rent_price_max)

    if filters.surface_min is not None:
        query = query.filter(Property.surface_area >= filters.surface_min)
    if filters.bedrooms_min is not None:
        query = query.filter(Property.bedrooms >= filters.bedrooms_min)
    if filters.property_type:
        query = query.filter(Property.property_type == filters.property_type)

    boolean_filters = [
        ("has_garden", filters.has_garden),
        ("has_terrace", filters.has_terrace),
        ("has_elevator", filters.has_elevator),
        ("has_parking", filters.has_parking),
        ("has_pool", filters.has_pool),
    ]
    for attr, value in boolean_filters:
        if value is not None:
            query = query.filter(getattr(Property, attr) == value)

    query = query.filter(Property.is_active == True)
    total = query.count()

    sort_column = getattr(Property, filters.sort_by, Property.created_at)
    query = query.order_by(
        sort_column.asc() if filters.sort_order == "asc" else sort_column.desc()
    )

    skip = (filters.page - 1) * filters.page_size
    properties = query.offset(skip).limit(filters.page_size).all()

    items = []
    for prop in properties:
        items.append(schemas.PropertySummaryResponse.model_validate(prop))

    return schemas.PaginatedPropertiesResponse(
        items=items,
        total=total,
        page=filters.page,
        page_size=filters.page_size,
        total_pages=math.ceil(total / filters.page_size),
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

    # --------------------
    # Localisation
    # --------------------
    if filters.city:
        query = query.filter(Property.city == filters.city)

    if filters.postal_code:
        query = query.filter(Property.postal_code == filters.postal_code)

    if filters.district:
        query = query.filter(Property.district == filters.district)

    if filters.neighborhood:
        query = query.filter(Property.neighborhood == filters.neighborhood)

    # --------------------
    # Transaction
    # --------------------
    if filters.transaction_type:
        query = query.filter(Property.transaction_type == filters.transaction_type)

    # --------------------
    # Prix (vente)
    # --------------------
    if filters.price_min is not None:
        query = query.filter(Property.price >= filters.price_min)

    if filters.price_max is not None:
        query = query.filter(Property.price <= filters.price_max)

    if filters.price_per_sqm_min is not None:
        query = query.filter(Property.price_per_sqm >= filters.price_per_sqm_min)

    if filters.price_per_sqm_max is not None:
        query = query.filter(Property.price_per_sqm <= filters.price_per_sqm_max)

    # --------------------
    # Prix (location)
    # --------------------
    if filters.rent_price_min is not None:
        query = query.filter(Property.rent_price_monthly >= filters.rent_price_min)

    if filters.rent_price_max is not None:
        query = query.filter(Property.rent_price_monthly <= filters.rent_price_max)

    # --------------------
    # Surfaces & pièces
    # --------------------
    if filters.surface_min is not None:
        query = query.filter(Property.surface_area >= filters.surface_min)

    if filters.surface_max is not None:
        query = query.filter(Property.surface_area <= filters.surface_max)

    if filters.rooms_min is not None:
        query = query.filter(Property.rooms >= filters.rooms_min)

    if filters.bedrooms_min is not None:
        query = query.filter(Property.bedrooms >= filters.bedrooms_min)

    if filters.bathrooms_min is not None:
        query = query.filter(Property.bathrooms >= filters.bathrooms_min)

    if filters.toilets_min is not None:
        query = query.filter(Property.toilets >= filters.toilets_min)

    if filters.floors_min is not None:
        query = query.filter(Property.floors >= filters.floors_min)

    # --------------------
    # Type de bien
    # --------------------
    if filters.property_type:
        query = query.filter(Property.property_type == filters.property_type)

    # --------------------
    # Équipements
    # --------------------
    if filters.has_garden is not None:
        query = query.filter(Property.has_garden == filters.has_garden)

    if filters.has_terrace is not None:
        query = query.filter(Property.has_terrace == filters.has_terrace)

    if filters.has_balcony is not None:
        query = query.filter(Property.has_balcony == filters.has_balcony)

    if filters.has_parking is not None:
        query = query.filter(Property.has_parking == filters.has_parking)

    if filters.has_cave is not None:
        query = query.filter(Property.has_cave == filters.has_cave)

    if filters.has_elevator is not None:
        query = query.filter(Property.has_elevator == filters.has_elevator)

    if filters.has_pool is not None:
        query = query.filter(Property.has_pool == filters.has_pool)

    if filters.is_quiet is not None:
        query = query.filter(Property.is_quiet == filters.is_quiet)

    if filters.is_furnished is not None:
        query = query.filter(Property.is_furnished == filters.is_furnished)

    # --------------------
    # Parking / étage
    # --------------------
    if filters.parking_spaces_min is not None:
        query = query.filter(Property.parking_spaces >= filters.parking_spaces_min)

    if filters.floor_number_min is not None:
        query = query.filter(Property.floor_number >= filters.floor_number_min)

    # --------------------
    # Année / disponibilité
    # --------------------
    if filters.construction_year_min is not None:
        query = query.filter(
            Property.construction_year >= filters.construction_year_min
        )

    if filters.available_from is not None:
        query = query.filter(Property.available_from >= filters.available_from)

    # --------------------
    # Énergie
    # --------------------
    if filters.energy_rating:
        query = query.filter(Property.energy_rating == filters.energy_rating)

    if filters.heating_type:
        query = query.filter(Property.heating_type == filters.heating_type)

    # --------------------
    # Métadonnées
    # --------------------
    if filters.is_active is not None:
        query = query.filter(Property.is_active == filters.is_active)

    return query.count()


def get_property_by_id(property_id: UUID, db: Session):
    property = (
        db.query(Property)
        .options(joinedload(Property.photos))
        .filter(Property.id == property_id)
        .first()
    )

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


def get_properties_by_cities(
    cities: list[str],
    db: Session,
    transaction_type: TransactionType,
    page_size: int = 10,
    sort_by: str = "created_at",
    sort_order: str = "desc",
) -> dict[str, schemas.CityPropertiesResponse]:
    results = {}

    for city in cities:
        filters = schemas.PropertyFilterParams(
            city=city,
            transaction_type=transaction_type,
            page=1,
            page_size=page_size,
            sort_by=sort_by,
            sort_order=sort_order,
            is_active=True,
        )

        paginated_response = search_properties(db, filters)

        results[city] = schemas.CityPropertiesResponse(
            city=city,
            properties=paginated_response.items,
            total=paginated_response.total,
        )

    return results
