from fastapi import APIRouter, Query
from uuid import UUID
from app.database.core import DbSession
from app.admin.properties import schemas, service
from app.properties import schemas as property_schemas

router = APIRouter(prefix="/admin/properties", tags=["Admin - Properties"])


@router.get("", response_model=schemas.AdminPropertiesResponse)
async def get_admin_properties(
    db: DbSession,
    search: str | None = Query(
        default=None, description="Recherche sur le titre ou la référence"
    ),
    transaction_type: str | None = Query(default=None, description="'sale' ou 'rent'"),
    status: str | None = Query(default=None, description="'active' ou 'inactive'"),
    city: str | None = Query(default=None, description="Filtrer par ville"),
    energy_rating: str | None = Query(
        default=None, description="A, B, C, D, E, F ou G"
    ),
    price_min: int | None = Query(default=None, description="Prix minimum"),
    price_max: int | None = Query(default=None, description="Prix maximum"),
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=20, ge=1, le=100),
):
    """Liste paginée et filtrée de toutes les propriétés."""
    return service.get_admin_properties(
        db=db,
        search=search,
        transaction_type=transaction_type,
        status_filter=status,
        city=city,
        energy_rating=energy_rating,
        price_min=price_min,
        price_max=price_max,
        page=page,
        limit=limit,
    )


@router.get("/agent/{agent_id}", response_model=schemas.AdminPropertiesResponse)
async def get_agent_properties(
    agent_id: UUID,
    db: DbSession,
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=20, ge=1, le=100),
):
    """Liste des propriétés d'un agent spécifique."""
    return service.get_agent_properties(
        agent_id=agent_id, db=db, page=page, limit=limit
    )


@router.get("/{property_id}", response_model=property_schemas.PropertyResponse)
async def get_property_by_id(property_id: UUID, db: DbSession):
    """Détail complet d'une propriété."""
    return service.get_property_by_id(property_id=property_id, db=db)


@router.patch("/{property_id}", response_model=property_schemas.PropertyResponse)
async def update_property(
    property_id: UUID,
    update_data: property_schemas.UpdatePropertyRequest,
    db: DbSession,
):
    """Mise à jour d'une propriété par l'admin."""
    return service.update_property(
        property_id=property_id, update_data=update_data, db=db
    )


@router.delete("/{property_id}", status_code=204)
async def delete_property(property_id: UUID, db: DbSession):
    """Suppression d'une propriété par l'admin."""
    service.delete_property(property_id=property_id, db=db)
