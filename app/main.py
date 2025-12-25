from fastapi import FastAPI
from .api import register_routes
from app.logging_config import configure_logging, LogLevels
from contextlib import asynccontextmanager
from app.database.core import engine, Base
from app.entities import *

configure_logging(LogLevels.debug)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Démarrage de l'application...")

    Base.metadata.create_all(bind=engine)
    print("✅ Tables vérifiées/créées dans la base de données")

    yield

    print("👋 Arrêt de l'application...")


app = FastAPI(
    title="Real Estate API",
    description="API pour la gestion immobilière",
    version="1.0.0",
    lifespan=lifespan
)


register_routes(app)
