from typing import Annotated
from fastapi import APIRouter, Depends, Path, status
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
