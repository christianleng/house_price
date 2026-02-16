from uuid import UUID
from pydantic import BaseModel, ConfigDict

from app.entities.enum import EnergyRating, TransactionType


class StagnantPropertyResponse(BaseModel):
    id: UUID
    reference: str
    title: str
    city: str
    transaction_type: TransactionType
    price: int | None
    rent_price_monthly: int | None
    energy_rating: EnergyRating | None
    days_stagnant: int
    thumbnail_url: str | None

    model_config = ConfigDict(from_attributes=True)


class QualityScoreResponse(BaseModel):
    photos: int  # % biens avec au moins 1 photo
    description: int  # % biens avec description renseignée
    price: int  # % biens avec prix renseigné
    energy_rating: int  # % biens avec DPE renseigné
    surface: int  # toujours 100 car non nullable
    global_score: int  # moyenne pondérée des 5 critères


class PropertyGlobalStatsResponse(BaseModel):
    # --- Totaux ---
    total: int
    active: int
    inactive: int

    # --- Par type de transaction ---
    for_sale: int
    for_rent: int

    # --- Prix moyens ---
    avg_sale_price: float | None
    avg_rent_price: float | None

    # --- Qualité du catalogue ---
    without_photos: int  # photos_count == 0
    without_price: int  # price IS NULL AND rent_price_monthly IS NULL

    # --- Répartition DPE ---
    by_energy_rating: dict[str, int]  # {"A": 5, "B": 12, ...}

    # --- Répartition par type de bien ---
    by_property_type: dict[str, int]  # {"apartment": 30, "house": 12, ...}

    # --- Répartition par ville (top 10) ---
    by_city: dict[str, int]  # {"Paris": 20, "Lyon": 8, ...}
    at_risk_dpe: int
    available_soon: int
    avg_age_days: float | None

    avg_sale_delay_days: float | None
    stagnant_properties: list[StagnantPropertyResponse]
    quality_score: QualityScoreResponse
    price_per_sqm_by_city: dict[str, float]


class MonthlyStatsPeriod(BaseModel):
    month: str  # format "2025-09"
    added: int
    for_sale: int
    for_rent: int


class PropertyMonthlyStatsResponse(BaseModel):
    periods: list[MonthlyStatsPeriod]
    # Variation calculée entre le dernier et l'avant-dernier mois
    trend_percent: float | None  # +12.5 ou -8.0, None si pas assez de données


class CityPerformanceResponse(BaseModel):
    city: str
    nb_biens: int
    avg_price_per_sqm: float | None
    avg_sale_delay: float | None


class CitiesPerformanceStatsResponse(BaseModel):
    cities: list[CityPerformanceResponse]
