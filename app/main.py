from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from contextlib import asynccontextmanager

from .api import register_routes
from app.logging_config import configure_logging, LogLevels
from app.database.core import engine, Base
from app.entities import *

configure_logging(LogLevels.debug)


BASE_UPLOAD_DIR = Path("uploads")
PHOTOS_UPLOAD_DIR = BASE_UPLOAD_DIR / "photos"

PHOTOS_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Démarrage de l'application...")

    Base.metadata.create_all(bind=engine)
    print("✅ Tables vérifiées/créées dans la base de données")

    yield

    print("👋 Arrêt de l'application...")


app = FastAPI(
    title="House Price API",
    description="API pour la gestion immobilière",
    version="1.0.0",
    lifespan=lifespan,
    docs_url=None,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/uploads", StaticFiles(directory=BASE_UPLOAD_DIR), name="uploads")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_ui_parameters={"persistAuthorization": True},
    )


register_routes(app)
