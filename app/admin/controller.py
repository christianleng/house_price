from fastapi import APIRouter, Query
from app.database.core import DbSession
from app.admin import schemas, service

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/stats", response_model=schemas.PropertyGlobalStatsResponse)
async def get_global_stats(db: DbSession):
    """
    Statistiques globales du portefeuille pour le dashboard admin.
    Réservé aux admins — ne pas exposer aux agents.
    """
    return service.get_global_stats(db)


@router.get("/stats/monthly", response_model=schemas.PropertyMonthlyStatsResponse)
async def get_monthly_stats(
    db: DbSession,
    months: int = Query(
        default=6,
        ge=1,
        le=24,
        description="Nombre de mois à remonter (1-24)",
    ),
):
    """
    Évolution mensuelle sur N mois pour le dashboard admin.
    """
    return service.get_monthly_stats(db, months)


@router.get("/stats/cities", response_model=schemas.CitiesPerformanceStatsResponse)
async def get_cities_performance(db: DbSession):
    """
    Indicateurs clés par ville : nb biens, prix au m², délai moyen de vente.
    """
    return service.get_cities_performance(db)
