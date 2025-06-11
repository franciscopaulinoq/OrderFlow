from fastapi import APIRouter

from app.api.v1.endpoints import orders, product_orders

api_router = APIRouter()
api_router.include_router(orders.router)
api_router.include_router(product_orders.router)