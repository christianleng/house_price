from sqlalchemy.orm import Session
from app.entities.enum import EnergyRating, TransactionType
from app.entities.properties import Property
from app.admin import schemas

from sqlalchemy import func, extract, case
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta


def get_global_stats(db: Session) -> schemas.PropertyGlobalStatsResponse:
    """
    Retourne les statistiques globales du portefeuille.
    Un seul appel DB via des agrégats SQL — pas de N+1.
    """

    now = datetime.now(timezone.utc)
    in30d = now + timedelta(days=30)

    at_risk_dpe = (
        db.query(func.count(Property.id))
        .filter(
            Property.transaction_type == TransactionType.RENT,
            Property.energy_rating.in_([EnergyRating.F, EnergyRating.G]),
            Property.is_active == True,
        )
        .scalar()
    )

    available_soon = (
        db.query(func.count(Property.id))
        .filter(
            Property.available_from >= now,
            Property.available_from <= in30d,
            Property.is_active == True,
        )
        .scalar()
    )

    avg_age_days = (
        db.query(
            func.avg(func.extract("epoch", func.now() - Property.created_at) / 86400)
        )
        .filter(Property.is_active == True)
        .scalar()
    )

    stats = db.query(
        func.count(Property.id).label("total"),
        func.count(case((Property.is_active == True, 1))).label("active"),
        func.count(case((Property.is_active == False, 1))).label("inactive"),
        func.count(case((Property.transaction_type == TransactionType.SALE, 1))).label(
            "for_sale"
        ),
        func.count(case((Property.transaction_type == TransactionType.RENT, 1))).label(
            "for_rent"
        ),
        func.avg(
            case((Property.transaction_type == TransactionType.SALE, Property.price))
        ).label("avg_sale_price"),
        func.avg(
            case(
                (
                    Property.transaction_type == TransactionType.RENT,
                    Property.rent_price_monthly,
                )
            )
        ).label("avg_rent_price"),
        func.count(case((Property.photos_count == 0, 1))).label("without_photos"),
        func.count(
            case(((Property.price == None) & (Property.rent_price_monthly == None), 1))
        ).label("without_price"),
    ).one()

    # --- Répartition DPE ---
    energy_rows = (
        db.query(
            Property.energy_rating.label("rating"),
            func.count(Property.id).label("count"),
        )
        .filter(Property.energy_rating != None)
        .group_by(Property.energy_rating)
        .all()
    )
    by_energy_rating = {
        str(row.rating.value if hasattr(row.rating, "value") else row.rating): row.count
        for row in energy_rows
    }

    # --- Répartition par type de bien ---
    type_rows = (
        db.query(
            Property.property_type.label("ptype"),
            func.count(Property.id).label("count"),
        )
        .group_by(Property.property_type)
        .all()
    )
    by_property_type = {
        str(row.ptype.value if hasattr(row.ptype, "value") else row.ptype): row.count
        for row in type_rows
    }

    # --- Répartition par ville (top 10) ---
    city_rows = (
        db.query(
            Property.city.label("city"),
            func.count(Property.id).label("count"),
        )
        .group_by(Property.city)
        .order_by(func.count(Property.id).desc())
        .limit(10)
        .all()
    )
    by_city = {row.city: row.count for row in city_rows}

    avg_sale_delay_days = (
        db.query(
            func.avg(func.extract("epoch", func.now() - Property.created_at) / 86400)
        )
        .filter(
            Property.transaction_type == TransactionType.SALE,
            Property.is_active == True,
        )
        .scalar()
    )

    stagnant_threshold = now - timedelta(days=60)

    stagnant_rows = (
        db.query(Property)
        .filter(
            Property.is_active == True,
            Property.updated_at <= stagnant_threshold,
        )
        .order_by(Property.updated_at.asc())
        .limit(5)
        .all()
    )

    stagnant_properties = [
        schemas.StagnantPropertyResponse(
            id=p.id,
            reference=p.reference,
            title=p.title,
            city=p.city,
            transaction_type=p.transaction_type,
            price=p.price,
            rent_price_monthly=p.rent_price_monthly,
            energy_rating=p.energy_rating,
            days_stagnant=int((now - p.updated_at.replace(tzinfo=timezone.utc)).days),
            thumbnail_url=p.thumbnail_url,
        )
        for p in stagnant_rows
    ]
    total_active = (
        db.query(func.count(Property.id)).filter(Property.is_active == True).scalar()
        or 1
    )

    with_photos = (
        db.query(func.count(Property.id))
        .filter(
            Property.is_active == True,
            Property.photos_count > 0,
        )
        .scalar()
    )

    with_description = (
        db.query(func.count(Property.id))
        .filter(
            Property.is_active == True,
            Property.description != None,
            Property.description != "",
        )
        .scalar()
    )

    with_price = (
        db.query(func.count(Property.id))
        .filter(
            Property.is_active == True,
            (Property.price != None) | (Property.rent_price_monthly != None),
        )
        .scalar()
    )

    with_dpe = (
        db.query(func.count(Property.id))
        .filter(
            Property.is_active == True,
            Property.energy_rating != None,
        )
        .scalar()
    )

    score_photos = round((with_photos / total_active) * 100)
    score_description = round((with_description / total_active) * 100)
    score_price = round((with_price / total_active) * 100)
    score_dpe = round((with_dpe / total_active) * 100)
    score_surface = 100

    global_score = round(
        (score_photos + score_description + score_price + score_dpe + score_surface) / 5
    )

    quality_score = schemas.QualityScoreResponse(
        photos=score_photos,
        description=score_description,
        price=score_price,
        energy_rating=score_dpe,
        surface=score_surface,
        global_score=global_score,
    )

    price_sqm_rows = (
        db.query(
            Property.city,
            func.avg(Property.price_per_sqm).label("avg_price_per_sqm"),
        )
        .filter(
            Property.price_per_sqm != None,
            Property.is_active == True,
        )
        .group_by(Property.city)
        .order_by(func.avg(Property.price_per_sqm).desc())
        .all()
    )

    price_per_sqm_by_city = {
        row.city: round(float(row.avg_price_per_sqm), 0) for row in price_sqm_rows
    }

    return schemas.PropertyGlobalStatsResponse(
        total=stats.total,
        active=stats.active,
        inactive=stats.inactive,
        for_sale=stats.for_sale,
        for_rent=stats.for_rent,
        avg_sale_price=(
            round(float(stats.avg_sale_price), 0) if stats.avg_sale_price else None
        ),
        avg_rent_price=(
            round(float(stats.avg_rent_price), 0) if stats.avg_rent_price else None
        ),
        without_photos=stats.without_photos,
        without_price=stats.without_price,
        by_energy_rating=by_energy_rating,
        by_property_type=by_property_type,
        by_city=by_city,
        at_risk_dpe=at_risk_dpe or 0,
        available_soon=available_soon or 0,
        avg_age_days=round(float(avg_age_days), 1) if avg_age_days else None,
        avg_sale_delay_days=(
            round(float(avg_sale_delay_days), 1) if avg_sale_delay_days else None
        ),
        stagnant_properties=stagnant_properties,
        quality_score=quality_score,
        price_per_sqm_by_city=price_per_sqm_by_city,
    )


def get_monthly_stats(
    db: Session,
    months: int = 6,
) -> schemas.PropertyMonthlyStatsResponse:
    """
    Retourne l'évolution mensuelle des ajouts sur N mois.
    Calcule aussi la tendance % entre le dernier et l'avant-dernier mois.
    """

    # On remonte N mois en arrière depuis maintenant
    now = datetime.now(timezone.utc)
    start = now - relativedelta(months=months)

    rows = (
        db.query(
            extract("year", Property.created_at).label("year"),
            extract("month", Property.created_at).label("month"),
            func.count(Property.id).label("added"),
            func.count(
                case((Property.transaction_type == TransactionType.SALE, 1))
            ).label("for_sale"),
            func.count(
                case((Property.transaction_type == TransactionType.RENT, 1))
            ).label("for_rent"),
        )
        .filter(Property.created_at >= start)
        .group_by(
            extract("year", Property.created_at),
            extract("month", Property.created_at),
        )
        .order_by(
            extract("year", Property.created_at).asc(),
            extract("month", Property.created_at).asc(),
        )
        .all()
    )

    periods = [
        schemas.MonthlyStatsPeriod(
            month=f"{int(row.year):04d}-{int(row.month):02d}",
            added=row.added,
            for_sale=row.for_sale,
            for_rent=row.for_rent,
        )
        for row in rows
    ]

    # --- Calcul de la tendance % ---
    trend_percent: float | None = None
    if len(periods) >= 2:
        last = periods[-1].added
        previous = periods[-2].added
        if previous > 0:
            trend_percent = round(((last - previous) / previous) * 100, 1)
        elif last > 0:
            trend_percent = 100.0  # de 0 à N = +100%

    return schemas.PropertyMonthlyStatsResponse(
        periods=periods,
        trend_percent=trend_percent,
    )


def get_cities_performance(db: Session) -> schemas.CitiesPerformanceStatsResponse:
    """
    Retourne les indicateurs clés par ville :
    - nombre de biens actifs
    - prix moyen au m²
    - délai moyen de vente (jours depuis created_at sur les ventes actives)
    """

    # --- Count + avg price_per_sqm par ville ---
    city_rows = (
        db.query(
            Property.city.label("city"),
            func.count(Property.id).label("nb_biens"),
            func.avg(Property.price_per_sqm).label("avg_price_per_sqm"),
        )
        .filter(Property.is_active == True)
        .group_by(Property.city)
        .order_by(func.count(Property.id).desc())
        .all()
    )

    # --- Délai moyen de vente par ville (ventes uniquement) ---
    delay_rows = (
        db.query(
            Property.city.label("city"),
            func.avg(
                func.extract("epoch", func.now() - Property.created_at) / 86400
            ).label("avg_sale_delay"),
        )
        .filter(
            Property.transaction_type == TransactionType.SALE,
            Property.is_active == True,
        )
        .group_by(Property.city)
        .all()
    )

    delay_by_city = {
        row.city: round(float(row.avg_sale_delay), 1) if row.avg_sale_delay else None
        for row in delay_rows
    }

    cities = [
        schemas.CityPerformanceResponse(
            city=row.city,
            nb_biens=row.nb_biens,
            avg_price_per_sqm=(
                round(float(row.avg_price_per_sqm), 0)
                if row.avg_price_per_sqm
                else None
            ),
            avg_sale_delay=delay_by_city.get(row.city),
        )
        for row in city_rows
    ]

    return schemas.CitiesPerformanceStatsResponse(cities=cities)
