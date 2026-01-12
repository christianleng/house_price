from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile, status
from uuid import UUID, uuid4
from PIL import Image
import io
import time
import logging
from pathlib import Path
from datetime import timezone

from app.entities.photo import Photo
from app.entities.properties import Property
from app.photos import schemas


IMAGE_SIZES = {
    "thumbnail": (150, 150),
    "small": (400, 300),
    "medium": (800, 600),
    "large": (1200, 900),
}

ALLOWED_CONTENT_TYPES = [
    "image/jpeg",
    "image/jpg",
    "image/png",
    "image/webp",
    "image/gif",
]

MAX_FILE_SIZE = 10 * 1024 * 1024

JPEG_QUALITY = 85
WEBP_QUALITY = 80

UPLOAD_DIR = Path("uploads/photos")


# ============== Image Processing ==============


class ImageProcessor:
    @staticmethod
    def validate_image(file: UploadFile) -> None:
        if file.content_type not in ALLOWED_CONTENT_TYPES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid file type. Allowed: {', '.join(ALLOWED_CONTENT_TYPES)}",
            )

        if file.size and file.size > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"File too large. Maximum size: {MAX_FILE_SIZE // (1024*1024)}MB",
            )

    @staticmethod
    def process_image(image_data: bytes, filename: str) -> dict:
        start_time = time.time()

        try:
            image = Image.open(io.BytesIO(image_data))
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid image file: {str(e)}",
            )

        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        original_width, original_height = image.size

        file_id = str(uuid4())[:8]
        base_name = Path(filename).stem

        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

        urls = {
            "original_width": original_width,
            "original_height": original_height,
        }

        original_filename = f"{file_id}_{base_name}_original.jpg"
        original_path = UPLOAD_DIR / original_filename
        image.save(original_path, "JPEG", quality=JPEG_QUALITY, optimize=True)
        urls["url_original"] = f"/uploads/photos/{original_filename}"

        for size_name, (width, height) in IMAGE_SIZES.items():
            resized = ImageProcessor._resize_image(image.copy(), width, height)

            jpeg_filename = f"{file_id}_{base_name}_{size_name}.jpg"
            jpeg_path = UPLOAD_DIR / jpeg_filename
            resized.save(jpeg_path, "JPEG", quality=JPEG_QUALITY, optimize=True)
            urls[f"url_{size_name}"] = f"/uploads/photos/{jpeg_filename}"

            webp_filename = f"{file_id}_{base_name}_{size_name}.webp"
            webp_path = UPLOAD_DIR / webp_filename
            resized.save(webp_path, "WEBP", quality=WEBP_QUALITY, optimize=True)
            urls[f"url_{size_name}_webp"] = f"/uploads/photos/{webp_filename}"

        processing_time = int((time.time() - start_time) * 1000)
        urls["processing_time_ms"] = processing_time

        logging.info(f"✅ Image processed: {filename} in {processing_time}ms")

        return urls

    @staticmethod
    def _resize_image(
        image: Image.Image, max_width: int, max_height: int
    ) -> Image.Image:
        original_width, original_height = image.size

        width_ratio = max_width / original_width
        height_ratio = max_height / original_height

        ratio = max(width_ratio, height_ratio)

        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)

        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        left = (new_width - max_width) // 2
        top = (new_height - max_height) // 2
        right = left + max_width
        bottom = top + max_height

        return image.crop((left, top, right, bottom))

    @staticmethod
    def delete_image_files(photo: Photo) -> None:
        urls_to_delete = [
            photo.url_original,
            photo.url_thumbnail,
            photo.url_small,
            photo.url_medium,
            photo.url_large,
            photo.url_thumbnail_webp,
            photo.url_small_webp,
            photo.url_medium_webp,
            photo.url_large_webp,
            photo.url,
        ]

        for url in urls_to_delete:
            if url:
                file_path = Path(url.lstrip("/"))
                if file_path.exists():
                    try:
                        file_path.unlink()
                        logging.info(f"🗑️ Deleted: {file_path}")
                    except Exception as e:
                        logging.warning(f"⚠️ Failed to delete {file_path}: {e}")


def upload_photo(
    property_id: UUID,
    file: UploadFile,
    agent_id: UUID,
    db: Session,
    meta: schemas.PhotoUploadMeta | None = None,
) -> schemas.PhotoUploadResponse:
    prop = db.query(Property).filter(Property.id == property_id).first()

    if not prop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Property not found"
        )

    if prop.agent_id != agent_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only add photos to your own properties",
        )

    # Valider le fichier
    ImageProcessor.validate_image(file)

    # Lire le contenu du fichier
    image_data = file.file.read()
    file_size = len(image_data)

    # Vérifier la taille après lecture
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File too large. Maximum size: {MAX_FILE_SIZE // (1024*1024)}MB",
        )

    # Traiter l'image
    urls = ImageProcessor.process_image(image_data, file.filename)

    # Déterminer l'ordre d'affichage
    if meta and meta.display_order is not None:
        display_order = meta.display_order
    else:
        # Obtenir le prochain ordre disponible
        max_order = db.query(Photo).filter(Photo.property_id == property_id).count()
        display_order = max_order

    # Si c'est la première photo ou is_primary, mettre les autres à false
    is_primary = meta.is_primary if meta else False
    if is_primary:
        db.query(Photo).filter(Photo.property_id == property_id).update(
            {"is_primary": False}
        )

    # Si c'est la première photo, la mettre en primary automatiquement
    existing_photos = db.query(Photo).filter(Photo.property_id == property_id).count()
    if existing_photos == 0:
        is_primary = True

    # Créer l'entrée en base
    new_photo = Photo(
        id=uuid4(),
        property_id=property_id,
        url=urls.get("url_medium"),  # Legacy fallback
        url_original=urls.get("url_original"),
        url_thumbnail=urls.get("url_thumbnail"),
        url_small=urls.get("url_small"),
        url_medium=urls.get("url_medium"),
        url_large=urls.get("url_large"),
        url_thumbnail_webp=urls.get("url_thumbnail_webp"),
        url_small_webp=urls.get("url_small_webp"),
        url_medium_webp=urls.get("url_medium_webp"),
        url_large_webp=urls.get("url_large_webp"),
        has_webp=True,
        original_filename=file.filename,
        original_width=urls.get("original_width"),
        original_height=urls.get("original_height"),
        size_bytes=file_size,
        content_type=file.content_type,
        is_primary=is_primary,
        display_order=display_order,
        caption=meta.caption if meta else None,
    )

    db.add(new_photo)
    db.commit()
    db.refresh(new_photo)

    logging.info(f"✅ Photo uploaded for property {property_id}")

    return schemas.PhotoUploadResponse(
        id=new_photo.id,
        message="Photo uploaded successfully",
        urls=schemas.PhotoUrls(
            thumbnail=schemas.PhotoUrlFormat(
                jpeg=new_photo.url_thumbnail, webp=new_photo.url_thumbnail_webp
            ),
            small=schemas.PhotoUrlFormat(
                jpeg=new_photo.url_small, webp=new_photo.url_small_webp
            ),
            medium=schemas.PhotoUrlFormat(
                jpeg=new_photo.url_medium, webp=new_photo.url_medium_webp
            ),
            large=schemas.PhotoUrlFormat(
                jpeg=new_photo.url_large, webp=new_photo.url_large_webp
            ),
            original=schemas.PhotoUrlFormat(jpeg=new_photo.url_original, webp=None),
        ),
        original_filename=new_photo.original_filename,
        size_bytes=new_photo.size_bytes,
        processing_time_ms=urls.get("processing_time_ms"),
    )


def upload_multiple_photos(
    property_id: UUID,
    files: list[UploadFile],
    agent_id: UUID,
    db: Session,
) -> schemas.MultiplePhotoUploadResponse:
    """
    Upload plusieurs photos à la fois.
    """
    uploaded = []
    failed = []

    for file in files:
        try:
            result = upload_photo(property_id, file, agent_id, db)
            uploaded.append(result)
        except HTTPException as e:
            failed.append(f"{file.filename}: {e.detail}")
        except Exception as e:
            failed.append(f"{file.filename}: {str(e)}")

    return schemas.MultiplePhotoUploadResponse(
        uploaded=uploaded,
        failed=failed,
        total_uploaded=len(uploaded),
        total_failed=len(failed),
    )


def get_property_photos(property_id: UUID, db: Session) -> list[schemas.PhotoResponse]:
    """
    Récupère toutes les photos d'une property.
    """
    photos = (
        db.query(Photo)
        .filter(Photo.property_id == property_id)
        .order_by(Photo.display_order)
        .all()
    )

    return [schemas.photo_to_response(p) for p in photos]


def get_photo_by_id(photo_id: UUID, db: Session) -> schemas.PhotoResponse:
    """
    Récupère une photo par son ID.
    """
    photo = db.query(Photo).filter(Photo.id == photo_id).first()

    if not photo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Photo not found"
        )

    return schemas.photo_to_response(photo)


def upload_photos(
    property_id: UUID, files: list[UploadFile], agent_id: UUID, db: Session
) -> list[schemas.PhotoResponse]:
    property = db.query(Property).filter(Property.id == property_id).first()

    if not property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Property not found"
        )

    if property.agent_id != agent_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only add photos to your own properties",
        )

    uploaded_photos = []

    for file in files:
        ImageProcessor.validate_image(file)

        image_data = file.file.read()
        processed = ImageProcessor.process_image(image_data, file.filename)

        photo = Photo(
            property_id=property_id,
            url_original=processed["url_original"],
            url_thumbnail=processed.get("url_thumbnail"),
            url_small=processed.get("url_small"),
            url_medium=processed.get("url_medium"),
            url_large=processed.get("url_large"),
            original_filename=file.filename,
            original_width=processed.get("original_width"),
            original_height=processed.get("original_height"),
            size_bytes=len(image_data),
            content_type=file.content_type,
            is_primary=False,
            display_order=property.photos_count,
        )

        db.add(photo)
        uploaded_photos.append(photo)

    property.photos_count += len(files)

    db.commit()

    logging.info(f"✅ Uploaded {len(files)} photos for property {property_id}")

    return [schemas.photo_to_response(p) for p in uploaded_photos]


def delete_photo(photo_id: UUID, agent_id: UUID, db: Session) -> None:
    photo = db.query(Photo).filter(Photo.id == photo_id).first()

    if not photo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Photo not found"
        )

    prop = db.query(Property).filter(Property.id == photo.property_id).first()

    if prop.agent_id != agent_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete photos from your own properties",
        )

    prop.photos_count -= 1

    db.delete(photo)
    db.commit()

    logging.info(f"✅ Photo deleted: {photo_id}")


def set_primary_photo(
    property_id: UUID, photo_id: UUID, agent_id: UUID, db: Session
) -> schemas.PhotoResponse:
    prop = db.query(Property).filter(Property.id == property_id).first()

    if not prop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Property not found"
        )

    if prop.agent_id != agent_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only modify your own properties",
        )

    photo = (
        db.query(Photo)
        .filter(Photo.id == photo_id, Photo.property_id == property_id)
        .first()
    )

    if not photo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Photo not found for this property",
        )

    db.query(Photo).filter(Photo.property_id == property_id).update(
        {"is_primary": False}
    )

    photo.is_primary = True
    db.commit()
    db.refresh(photo)

    logging.info(f"✅ Photo {photo_id} set as primary for property {property_id}")

    return schemas.photo_to_response(photo)


def reorder_photos(
    property_id: UUID, photo_ids: list[UUID], agent_id: UUID, db: Session
) -> list[schemas.PhotoResponse]:
    prop = db.query(Property).filter(Property.id == property_id).first()

    if not prop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Property not found"
        )

    if prop.agent_id != agent_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only modify your own properties",
        )

    existing_photos = db.query(Photo).filter(Photo.property_id == property_id).all()

    existing_ids = {str(p.id) for p in existing_photos}
    provided_ids = {str(pid) for pid in photo_ids}

    if existing_ids != provided_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Photo IDs don't match the property's photos",
        )

    for index, photo_id in enumerate(photo_ids):
        db.query(Photo).filter(Photo.id == photo_id).update({"display_order": index})

    db.commit()

    photos = (
        db.query(Photo)
        .filter(Photo.property_id == property_id)
        .order_by(Photo.display_order)
        .all()
    )

    logging.info(f"✅ Photos reordered for property {property_id}")

    return [schemas.photo_to_response(p) for p in photos]
