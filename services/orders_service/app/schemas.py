from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from .models import OrderStatus

class OrderCreate(BaseModel):
    client_id: str


class OrderOut(BaseModel):
    order_id: str
    client_id:str
    order_date: datetime
    total_value: float
    status: OrderStatus 
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ProductOrderCreate(BaseModel):
    order_id: str
    product_id: str
    quantity: int
    unit_price: float

class ProductOrderOut(BaseModel):
    product_order_id: str
    order_id: str 
    product_id: str
    quantity: int
    unit_price: float
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True