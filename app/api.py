from fastapi import FastAPI
from app.auth.controller import router as auth_router
from app.agents.controller import router as agents_router
from app.properties.controller import router as properties_router
from app.photos.controller import router as photos_router


def register_routes(app: FastAPI):
    app.include_router(auth_router, prefix="/api")
    app.include_router(agents_router, prefix="/api")
    app.include_router(properties_router, prefix="/api")
    app.include_router(photos_router, prefix="/api")
