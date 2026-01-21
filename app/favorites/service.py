from uuid import UUID
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.entities.favorites import Favorite
from app.entities.properties import Property


def add_favorite(db: Session, user_id: UUID, property_id: UUID):
    property_exists = db.query(Property.id).filter(Property.id == property_id).first()
    if not property_exists:
        raise HTTPException(status_code=404, detail="Property not found")

    existing_fav = (
        db.query(Favorite)
        .filter(Favorite.user_id == user_id, Favorite.property_id == property_id)
        .first()
    )

    if existing_fav:
        return existing_fav

    new_fav = Favorite(user_id=user_id, property_id=property_id)
    try:
        db.add(new_fav)
        db.commit()
        db.refresh(new_fav)
        return new_fav
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Could not add favorite")


def remove_favorite(db: Session, user_id: UUID, property_id: UUID):
    fav = (
        db.query(Favorite)
        .filter(Favorite.user_id == user_id, Favorite.property_id == property_id)
        .first()
    )

    if not fav:
        raise HTTPException(status_code=404, detail="Favorite not found")

    db.delete(fav)
    db.commit()


def get_user_favorites(db: Session, user_id: UUID, page: int = 1, page_size: int = 20):
    skip = (page - 1) * page_size

    query = (
        db.query(Property)
        .join(Favorite, Favorite.property_id == Property.id)
        .filter(Favorite.user_id == user_id)
        .options(joinedload(Property.photos))
        .order_by(Favorite.created_at.desc())
    )

    total = query.count()
    properties = query.offset(skip).limit(page_size).all()

    return properties, total


def is_property_favorited(db: Session, user_id: UUID, property_id: UUID) -> bool:
    count = (
        db.query(Favorite)
        .filter(Favorite.user_id == user_id, Favorite.property_id == property_id)
        .count()
    )
    return count > 0
