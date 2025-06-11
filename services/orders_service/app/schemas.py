from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from .models import OrderStatus

class OrderCreate(BaseModel):
    client_id: str
    product_id: str
    quantity: int


class OrderOut(BaseModel):
    order_id: str
    client_id:str
    product_id: str
    quantity: int
    order_date: datetime
    total_value: float
    status: OrderStatus 
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True