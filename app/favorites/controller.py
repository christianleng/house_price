from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from app.database.core import get_db
from app.auth.dependencies import CurrentUser
from app.favorites import service, schemas
from app.properties.schemas import PropertySummaryResponse

router = APIRouter(prefix="/favorites", tags=["Favorites"])


@router.get(
    "/", response_model=List[PropertySummaryResponse], summary="Get my favorites"
)
async def get_my_favorites(
    current_user: CurrentUser,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    properties, total = service.get_user_favorites(
        db, user_id=current_user.id, page=page, page_size=page_size
    )
    return properties


@router.post(
    "/{property_id}",
    response_model=schemas.FavoriteResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add property to favorites",
)
async def add_favorite(
    property_id: UUID,
    current_user: CurrentUser,
    db: Session = Depends(get_db),
):
    return service.add_favorite(db, user_id=current_user.id, property_id=property_id)


@router.delete(
    "/{property_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remove property from favorites",
)
async def remove_favorite(
    property_id: UUID, current_user: CurrentUser, db: Session = Depends(get_db)
):
    service.remove_favorite(db, user_id=current_user.id, property_id=property_id)
    return None
