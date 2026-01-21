from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from uuid import UUID
from app.agents.dependencies import CurrentAgent
from app.properties import schemas, service
from app.database.core import DbSession

router = APIRouter(prefix="/properties", tags=["Properties"])


@router.get("/", response_model=schemas.PaginatedPropertiesResponse)
async def search_properties(
    filters: Annotated[schemas.PropertyFilterParams, Depends()], db: DbSession
):
    return service.search_properties(db, filters)


@router.post(
    "/", response_model=schemas.PropertyResponse, status_code=status.HTTP_201_CREATED
)
async def create_properties(
    property_data: schemas.CreatePropertyRequest,
    current_agent: CurrentAgent,
    db: DbSession,
):
    return service.create_properties(property_data, current_agent.id, db)


@router.get("/count", response_model=int)
async def count_properties(
    filters: Annotated[schemas.PropertyFilterParams, Depends()], db: DbSession
):
    return service.count_properties(db, filters)


@router.get("/by-cities", response_model=schemas.CitiesPropertiesResponse)
async def get_properties_by_cities(
    cities: Annotated[
        list[str],
        Query(
            ...,
            description="Liste des villes (ex: Paris,Lyon,Marseille)",
            min_length=1,
            max_length=10,
        ),
    ],
    db: DbSession,
    transaction_type: schemas.TransactionType = Query(
        ..., description="Type de transaction"
    ),
    page_size: int = Query(
        10, ge=1, le=50, description="Nombre de propriétés par ville"
    ),
    sort_by: str = Query("created_at", description="Champ de tri"),
    sort_order: str = Query("desc", description="Ordre de tri"),
):
    if len(cities) > 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maximum 10 villes autorisées",
        )

    normalized_cities = [city.strip().capitalize() for city in cities]

    data = service.get_properties_by_cities(
        db=db,
        cities=normalized_cities,
        transaction_type=transaction_type,
        page_size=page_size,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    return schemas.CitiesPropertiesResponse(
        data=data, transaction_type=transaction_type
    )


@router.get("/{property_id}", response_model=schemas.PropertyResponse)
async def get_property_by_id(property_id: UUID, db: DbSession):
    return service.get_property_by_id(property_id, db)


@router.get("/agent/{agent_id}", response_model=schemas.PaginatedPropertiesResponse)
async def get_agent_properties(
    agent_id: Annotated[UUID, Path(description="ID de l'agent")],
    filters: Annotated[schemas.PropertyFilterParams, Depends()],
    db: DbSession,
):
    return service.get_agent_properties(agent_id, filters, db)


@router.patch("/{property_id}", response_model=schemas.PropertyResponse)
async def update_property(
    property_id: UUID,
    update_data: schemas.UpdatePropertyRequest,
    current_agent: CurrentAgent,
    db: DbSession,
):
    return service.update_property(property_id, update_data, current_agent.id, db)


@router.delete("/{property_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_property(
    property_id: UUID,
    current_agent: CurrentAgent,
    db: DbSession,
):
    service.delete_property(property_id, current_agent.id, db)
    return
