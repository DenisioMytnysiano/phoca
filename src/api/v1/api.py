from api.v1.endpoints import category, call
from fastapi import APIRouter

api_router = APIRouter(prefix="/api")
api_router.include_router(category.router, prefix="/category", tags=["Category"])
api_router.include_router(call.router, prefix="/call", tags=["Call"])