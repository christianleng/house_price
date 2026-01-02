from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from app.database.core import Base


class Photo(Base):
    __tablename__ = "photos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    property_id = Column(
        UUID(as_uuid=True),
        ForeignKey("properties.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    url_thumbnail = Column(String, nullable=True)  # 150x150
    url_small = Column(String, nullable=True)  # 400x300
    url_medium = Column(String, nullable=True)  # 800x600
    url_large = Column(String, nullable=True)  # 1200x900
    url_original = Column(String, nullable=False)  # Original

    has_webp = Column(Boolean, default=True)

    original_filename = Column(String(255), nullable=True)
    original_width = Column(Integer, nullable=True)
    original_height = Column(Integer, nullable=True)
    size_bytes = Column(Integer, nullable=True)
    content_type = Column(String(50), nullable=True)

    is_primary = Column(Boolean, default=False, index=True)
    display_order = Column(Integer, default=0)
    caption = Column(String, nullable=True)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    property = relationship("Property", back_populates="photos")

    def get_url(self, size: str = "medium", prefer_webp: bool = True) -> str:
        """
        Retourne l'URL de l'image selon la taille demandée.

        Args:
            size: 'thumbnail', 'small', 'medium', 'large', 'original'
            prefer_webp: Si True, retourne WebP si disponible
        """
        if prefer_webp and self.has_webp:
            webp_url = getattr(self, f"url_{size}_webp", None)
            if webp_url:
                return webp_url

        sized_url = getattr(self, f"url_{size}", None)
        if sized_url:
            return sized_url

        return self.url_original or self.url

    def to_urls_dict(self) -> dict:
        return {
            "thumbnail": {
                "jpeg": self.url_thumbnail,
                "webp": self.url_thumbnail_webp if self.has_webp else None,
            },
            "small": {
                "jpeg": self.url_small,
                "webp": self.url_small_webp if self.has_webp else None,
            },
            "medium": {
                "jpeg": self.url_medium,
                "webp": self.url_medium_webp if self.has_webp else None,
            },
            "large": {
                "jpeg": self.url_large,
                "webp": self.url_large_webp if self.has_webp else None,
            },
            "original": {
                "jpeg": self.url_original,
                "webp": None,
            },
        }
