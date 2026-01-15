from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List, Optional

from app.entities.enum import PropertyType, EnergyRating, HeatingType, TransactionType


class CreatePropertyRequest(BaseModel):
    reference: str = Field(
        ..., min_length=2, max_length=20, description="Référence unique de la propriété"
    )

    title: str = Field(
        ..., min_length=2, max_length=500, description="Titre de l'annonce"
    )
    description: str | None = Field(
        None, min_length=10, max_length=5000, description="Description détaillée"
    )

    address: str | None = Field(
        None, min_length=2, max_length=100, description="Adresse complète"
    )
    neighborhood: str = Field(..., min_length=2, max_length=100, description="Quartier")
    city: str = Field(..., min_length=2, max_length=100, description="Ville")
    district: str = Field(
        ..., min_length=2, max_length=20, description="Arrondissement"
    )
    postal_code: str = Field(
        ..., min_length=2, max_length=20, description="Code postal"
    )
    latitude: float = Field(..., ge=-90, le=90, description="Latitude GPS")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude GPS")

    price: int = Field(..., ge=1, le=10_000_000, description="Prix en euros")
    price_per_sqm: int = Field(..., ge=1, le=100_000, description="Prix au m² en euros")

    property_type: PropertyType = Field(..., description="Type de bien")
    surface_area: int = Field(..., ge=1, description="Surface habitable en m²")
    rooms: int = Field(..., ge=1, description="Nombre de pièces")
    bedrooms: int = Field(..., ge=0, description="Nombre de chambres")
    bathrooms: int | None = Field(None, ge=0, description="Nombre de salles de bain")
    toilets: int | None = Field(None, ge=0, description="Nombre de toilettes")
    floors: int | None = Field(None, ge=0, description="Nombre d'étages")

    floor_number: int | None = Field(None, ge=0, description="Étage de l'appartement")
    has_cave: bool = Field(False, description="Présence d'une cave")
    has_elevator: bool = Field(False, description="Présence d'un ascenseur")
    has_balcony: bool = Field(False, description="Présence d'un balcon")
    has_terrace: bool = Field(False, description="Présence d'une terrasse")
    has_garden: bool = Field(False, description="Présence d'un jardin")
    has_parking: bool = Field(False, description="Parking disponible")
    parking_spaces: int | None = Field(
        None, ge=0, description="Nombre de places de parking"
    )

    energy_rating: EnergyRating | None = Field(
        None, description="Classe énergétique (DPE)"
    )
    heating_type: HeatingType | None = Field(None, description="Type de chauffage")

    construction_year: int | None = Field(
        None, ge=1800, le=2100, description="Année de construction"
    )
    available_from: datetime | None = Field(None, description="Date de disponibilité")
    is_furnished: bool = Field(False, description="Meublé ou non")

    @field_validator("price_per_sqm")
    @classmethod
    def validate_price_per_sqm(cls, v: int, values) -> int:
        if v <= 0:
            raise ValueError("Price per sqm must be positive")
        return v

    @field_validator("bedrooms")
    @classmethod
    def validate_bedrooms(cls, v: int, info) -> int:
        if v < 0:
            raise ValueError("Bedrooms cannot be negative")
        return v


class PropertyResponse(BaseModel):
    id: UUID
    agent_id: UUID
    reference: str

    title: str
    description: str | None

    address: str | None
    neighborhood: str
    city: str
    district: str
    postal_code: str
    latitude: float
    longitude: float

    price: int
    price_per_sqm: int

    property_type: PropertyType
    surface_area: int
    rooms: int
    bedrooms: int
    bathrooms: int | None
    toilets: int | None
    floors: int | None

    floor_number: int | None = None

    has_cave: bool | None = None
    has_elevator: bool
    has_balcony: bool
    has_terrace: bool
    has_garden: bool
    has_parking: bool
    parking_spaces: int | None = None

    energy_rating: EnergyRating | None
    heating_type: HeatingType | None

    construction_year: int | None = None
    available_from: datetime | None = None
    is_furnished: bool | None = None

    created_at: datetime
    updated_at: datetime | None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class PropertyWithAgentResponse(PropertyResponse):
    agent_name: str
    agent_email: str
    agent_phone: str
    agency_name: str


class PropertySummaryResponse(BaseModel):
    # Identité
    id: UUID
    agent_id: UUID
    reference: str

    # Localisation
    title: str
    address: str | None
    neighborhood: str | None
    city: str
    district: str | None
    postal_code: str
    latitude: float | None
    longitude: float | None

    # Transaction
    transaction_type: TransactionType

    # Prix
    price: int | None
    price_per_sqm: int | None
    rent_price_monthly: int | None
    charges_included: bool | None
    deposit: int | None

    # Caractéristiques
    property_type: PropertyType
    surface_area: int
    rooms: int
    bedrooms: int
    bathrooms: int | None
    toilets: int | None
    floors: int | None
    floor_number: int | None

    # Équipements
    has_garden: bool
    has_terrace: bool
    has_balcony: bool
    has_parking: bool
    parking_spaces: int | None
    has_cave: bool
    has_elevator: bool
    has_pool: bool
    is_quiet: bool
    is_furnished: bool

    # Énergie
    energy_rating: EnergyRating | None
    heating_type: HeatingType | None

    photos_count: int
    thumbnail_url: str | None

    # Métadonnées
    construction_year: int | None
    available_from: datetime | None
    created_at: datetime
    updated_at: datetime | None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class UpdatePropertyRequest(BaseModel):
    reference: str | None = Field(None, min_length=2, max_length=20)
    title: str | None = Field(None, min_length=2, max_length=500)
    description: str | None = Field(None, min_length=10, max_length=5000)

    address: str | None = Field(None, min_length=2, max_length=100)
    neighborhood: str | None = Field(None, min_length=2, max_length=100)
    city: str | None = Field(None, min_length=2, max_length=100)
    district: str | None = Field(None, min_length=2, max_length=20)
    postal_code: str | None = Field(None, min_length=2, max_length=20)
    latitude: float | None = Field(None, ge=-90, le=90)
    longitude: float | None = Field(None, ge=-180, le=180)

    price: int | None = Field(None, ge=1, le=10_000_000)
    price_per_sqm: int | None = Field(None, ge=1, le=100_000)

    property_type: PropertyType | None = None
    surface_area: int | None = Field(None, ge=1)
    rooms: int | None = Field(None, ge=1)
    bedrooms: int | None = Field(None, ge=0)
    bathrooms: int | None = Field(None, ge=0)
    toilets: int | None = Field(None, ge=0)
    floors: int | None = Field(None, ge=0)

    floor_number: int | None = Field(None, ge=0)
    has_cave: bool | None = None
    has_elevator: bool | None = None
    has_balcony: bool | None = None
    has_terrace: bool | None = None
    has_garden: bool | None = None
    has_parking: bool | None = None
    parking_spaces: int | None = Field(None, ge=0)

    energy_rating: EnergyRating | None = None
    heating_type: HeatingType | None = None

    construction_year: int | None = Field(None, ge=1800, le=2100)
    available_from: datetime | None = None
    is_furnished: bool | None = None
    is_active: bool | None = None

    model_config = ConfigDict(from_attributes=True)


class PropertyFilterParams(BaseModel):
    # --------------------
    # Localisation
    # --------------------
    city: str | None = None
    postal_code: str | None = None
    district: str | None = None
    neighborhood: str | None = None

    # --------------------
    # Transaction
    # --------------------
    transaction_type: TransactionType | None = None

    # --------------------
    # Prix (vente)
    # --------------------
    price_min: int | None = Field(None, ge=0, description="Prix minimum")
    price_max: int | None = Field(None, ge=0, description="Prix maximum")

    price_per_sqm_min: int | None = Field(None, ge=0, description="Prix au m² minimum")
    price_per_sqm_max: int | None = Field(None, ge=0, description="Prix au m² maximum")

    # --------------------
    # Prix (location)
    # --------------------
    rent_price_min: int | None = Field(None, ge=0, description="Loyer mensuel minimum")
    rent_price_max: int | None = Field(None, ge=0, description="Loyer mensuel maximum")

    # --------------------
    # Surfaces & pièces
    # --------------------
    surface_min: int | None = Field(None, ge=0, description="Surface minimale en m²")
    surface_max: int | None = Field(None, ge=0, description="Surface maximale en m²")

    rooms_min: int | None = Field(None, ge=1, description="Nombre minimum de pièces")
    bedrooms_min: int | None = Field(
        None, ge=0, description="Nombre minimum de chambres"
    )
    bathrooms_min: int | None = Field(
        None, ge=0, description="Nombre minimum de salles de bain"
    )
    toilets_min: int | None = Field(
        None, ge=0, description="Nombre minimum de toilettes"
    )
    floors_min: int | None = Field(None, ge=0, description="Nombre minimum d'étages")

    # --------------------
    # Type de bien
    # --------------------
    property_type: PropertyType | None = None

    # --------------------
    # Équipements (booléens)
    # --------------------
    has_garden: bool | None = None
    has_terrace: bool | None = None
    has_balcony: bool | None = None
    has_parking: bool | None = None
    has_cave: bool | None = None
    has_elevator: bool | None = None
    has_pool: bool | None = None
    is_quiet: bool | None = None
    is_furnished: bool | None = None

    # --------------------
    # Parking / étage
    # --------------------
    parking_spaces_min: int | None = Field(
        None, ge=0, description="Nombre minimum de places de parking"
    )
    floor_number_min: int | None = Field(None, ge=0, description="Étage minimum")

    # --------------------
    # Année / disponibilité
    # --------------------
    construction_year_min: int | None = Field(
        None, ge=1800, le=2100, description="Année de construction minimale"
    )
    available_from: datetime | None = Field(None, description="Disponible à partir de")

    # --------------------
    # Énergie
    # --------------------
    energy_rating: EnergyRating | None = None
    heating_type: HeatingType | None = None

    # --------------------
    # Métadonnées
    # --------------------
    is_active: bool | None = None

    # --------------------
    # Tri & pagination
    # --------------------
    sort_by: str = Field(
        "created_at",
        description="Champ de tri (created_at, price, surface_area, price_per_sqm, rooms)",
    )
    sort_order: str = Field("desc", description="Ordre de tri (asc, desc)")
    page: int = Field(1, ge=1, description="Numéro de page")
    page_size: int = Field(20, ge=1, le=100, description="Nombre de résultats par page")

    # --------------------
    # Validators
    # --------------------
    @field_validator("sort_by")
    @classmethod
    def validate_sort_by(cls, v: str) -> str:
        allowed_fields = [
            "created_at",
            "price",
            "surface_area",
            "price_per_sqm",
            "rooms",
            "bedrooms",
        ]
        if v not in allowed_fields:
            raise ValueError(f"sort_by must be one of: {', '.join(allowed_fields)}")
        return v

    @field_validator("sort_order")
    @classmethod
    def validate_sort_order(cls, v: str) -> str:
        if v not in ("asc", "desc"):
            raise ValueError('sort_order must be "asc" or "desc"')
        return v


class PaginatedPropertiesResponse(BaseModel):
    items: List[PropertySummaryResponse]
    total: int
    page: int
    page_size: int
    total_pages: int

    model_config = ConfigDict(from_attributes=True)


class PropertyStatsResponse(BaseModel):
    property_id: UUID
    favorites_count: int
    days_online: int
    average_price_in_city: float | None
    price_comparison: str


class CitiesPropertiesRequest(BaseModel):
    cities: list[str] = Field(
        ..., min_items=1, max_items=10, description="Liste des villes"
    )
    transaction_type: TransactionType
    page_size: int = Field(
        default=10, ge=1, le=50, description="Nombre de propriétés par ville"
    )
    sort_by: str = Field(default="created_at")
    sort_order: str = Field(default="desc")


class CityPropertiesResponse(BaseModel):
    city: str
    properties: list[PropertySummaryResponse]
    total: int


class CitiesPropertiesResponse(BaseModel):
    data: dict[str, CityPropertiesResponse]
    transaction_type: TransactionType

    model_config = ConfigDict(from_attributes=True)
