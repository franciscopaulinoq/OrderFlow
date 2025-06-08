from fastapi import APIRouter

from app.api.v1.endpoints import clients

api_router = APIRouter()
api_router.include_router(clients.router)