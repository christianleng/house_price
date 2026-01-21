from fastapi import APIRouter, File, Form, UploadFile, status
from uuid import UUID

from app.agents.dependencies import CurrentAgent
from app.photos import schemas, service
from app.database.core import DbSession

router = APIRouter(prefix="/photos", tags=["Photos"])


@router.get(
    "/property/{property_id}",
    response_model=list[schemas.PhotoResponse],
    summary="Get Property Photos",
    description="Get all photos for a property. Public endpoint.",
)
async def get_property_photos(property_id: UUID, db: DbSession):
    return service.get_property_photos(property_id, db)


@router.get(
    "/{photo_id}",
    response_model=schemas.PhotoResponse,
    summary="Get Photo By Id",
    description="Get a single photo by its ID. Public endpoint.",
)
async def get_photo_by_id(photo_id: UUID, db: DbSession):
    return service.get_photo_by_id(photo_id, db)


@router.post(
    "/property/{property_id}",
    response_model=schemas.PhotoUploadResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Upload Photo",
    description="""
    Upload a photo for a property.
    
    The image will be automatically:
    - Resized to multiple sizes (thumbnail, small, medium, large)
    - Converted to WebP format for better performance
    - Optimized for web delivery
    
    Accepted formats: JPEG, PNG, WebP, GIF
    Maximum size: 10MB
    """,
)
async def upload_photos(
    property_id: UUID,
    current_agent: CurrentAgent,
    db: DbSession,
    file: UploadFile = File(..., description="Image file to upload"),
    is_primary: bool = Form(False, description="Set as primary photo"),
    caption: str | None = Form(None, description="Photo caption"),
):
    meta = schemas.PhotoUploadMeta(is_primary=is_primary, caption=caption)
    return service.upload_photos(property_id, file, current_agent.id, db, meta)


@router.post(
    "/property/{property_id}/multiple",
    response_model=schemas.MultiplePhotoUploadResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Upload Multiple Photos",
    description="Upload multiple photos at once for a property.",
)
async def upload_multiple_photos(
    property_id: UUID,
    current_agent: CurrentAgent,
    db: DbSession,
    files: list[UploadFile] = File(..., description="Image files to upload"),
):
    return service.upload_multiple_photos(property_id, files, current_agent.id, db)


@router.patch(
    "/{photo_id}",
    response_model=schemas.PhotoResponse,
    summary="Update Photo",
    description="Update photo metadata (caption, primary status, order).",
)
async def update_photo(
    photo_id: UUID,
    update_data: schemas.PhotoUpdate,
    current_agent: CurrentAgent,
    db: DbSession,
):
    return service.update_photo(photo_id, update_data, current_agent.id, db)


@router.delete(
    "/{photo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Photo",
    description="Delete a photo. Only the property owner can delete.",
)
async def delete_photo(
    photo_id: UUID,
    current_agent: CurrentAgent,
    db: DbSession,
):
    service.delete_photo(photo_id, current_agent.id, db)
    return


@router.post(
    "/property/{property_id}/primary",
    response_model=schemas.PhotoResponse,
    summary="Set Primary Photo",
    description="Set a photo as the primary/thumbnail photo for a property.",
)
async def set_primary_photo(
    property_id: UUID,
    request: schemas.SetPrimaryRequest,
    current_agent: CurrentAgent,
    db: DbSession,
):
    return service.set_primary_photo(
        property_id, request.photo_id, current_agent.id, db
    )


@router.post(
    "/property/{property_id}/reorder",
    response_model=list[schemas.PhotoResponse],
    summary="Reorder Photos",
    description="Reorder photos for a property by providing the photo IDs in the desired order.",
)
async def reorder_photos(
    property_id: UUID,
    request: schemas.PhotoReorderRequest,
    current_agent: CurrentAgent,
    db: DbSession,
):
    return service.reorder_photos(property_id, request.photo_ids, current_agent.id, db)
