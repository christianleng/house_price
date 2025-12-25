from fastapi import FastAPI
from app.auth.controller import router as auth_router
from app.agents.controller import router as agents_router


def register_routes(app: FastAPI):
    app.include_router(auth_router, prefix="/api")
    app.include_router(agents_router, prefix="/api")
