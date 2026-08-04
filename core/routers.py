# <NAME> - jero98772

from fastapi import APIRouter, FastAPI

from core.health.api.health import router as health_router


def configure_routers(fast_api: FastAPI):
    api_router = APIRouter(prefix="/api")
    api_router.include_router(health_router)
    v1_router = APIRouter(prefix="/v1")
    # v1_router.include_router()
    api_router.include_router(v1_router)
    fast_api.include_router(api_router)
