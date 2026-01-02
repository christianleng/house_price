from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class PhotoUrlFormat(BaseModel):
    jpeg: str | None = None
    webp: str | None = None


class PhotoUrls(BaseModel):
    thumbnail: PhotoUrlFormat | None = None  # 150x150
    small: PhotoUrlFormat | None = None  # 400x300
    medium: PhotoUrlFormat | None = None  # 800x600
    large: PhotoUrlFormat | None = None  # 1200x900
    original: PhotoUrlFormat | None = None  # Taille originale


class PhotoResponse(BaseModel):
    id: UUID
    property_id: UUID

    urls: PhotoUrls

    original_filename: str | None = None
    original_width: int | None = None
    original_height: int | None = None
    size_bytes: int | None = None
    content_type: str | None = None

    is_primary: bool
    display_order: int
    caption: str | None = None

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_orm_with_urls(cls, photo) -> "PhotoResponse":
        return cls(
            id=photo.id,
            property_id=photo.property_id,
            urls=PhotoUrls(
                thumbnail=PhotoUrlFormat(
                    jpeg=photo.url_thumbnail,
                    webp=photo.url_thumbnail_webp if photo.has_webp else None,
                ),
                small=PhotoUrlFormat(
                    jpeg=photo.url_small,
                    webp=photo.url_small_webp if photo.has_webp else None,
                ),
                medium=PhotoUrlFormat(
                    jpeg=photo.url_medium,
                    webp=photo.url_medium_webp if photo.has_webp else None,
                ),
                large=PhotoUrlFormat(
                    jpeg=photo.url_large,
                    webp=photo.url_large_webp if photo.has_webp else None,
                ),
                original=PhotoUrlFormat(
                    jpeg=photo.url_original or photo.url, webp=None
                ),
            ),
            original_filename=photo.original_filename,
            original_width=photo.original_width,
            original_height=photo.original_height,
            size_bytes=photo.size_bytes,
            content_type=photo.content_type,
            is_primary=photo.is_primary,
            display_order=photo.display_order,
            caption=photo.caption,
            created_at=photo.created_at,
        )


class PhotoSummaryResponse(BaseModel):
    id: UUID
    url_thumbnail: str | None = None
    url_medium: str | None = None
    is_primary: bool
    display_order: int

    model_config = ConfigDict(from_attributes=True)


class PhotoCreate(BaseModel):
    is_primary: bool = False
    display_order: int = 0
    caption: str | None = Field(None, max_length=255)


class PhotoUpdate(BaseModel):
    is_primary: bool | None = None
    display_order: int | None = None
    caption: str | None = Field(None, max_length=255)

    model_config = ConfigDict(from_attributes=True)


class PhotoReorderRequest(BaseModel):
    photo_ids: list[UUID] = Field(
        ..., description="Liste des IDs de photos dans l'ordre souhaité"
    )


class PhotoUploadResponse(BaseModel):

    id: UUID
    message: str = "Photo uploaded successfully"
    urls: PhotoUrls
    processing_time_ms: int | None = None


class PhotoUploadMeta(BaseModel):
    is_primary: bool = False
    display_order: int | None = None
    caption: str | None = Field(None, max_length=255)


class MultiplePhotoUploadResponse(BaseModel):
    uploaded: list[PhotoUploadResponse]
    failed: list[str]
    total_uploaded: int
    total_failed: int


def photo_to_response(photo) -> PhotoResponse:
    return PhotoResponse.from_orm_with_urls(photo)


class SetPrimaryRequest(BaseModel):
    photo_id: UUID
