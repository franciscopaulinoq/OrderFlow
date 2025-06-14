from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Annotated

from .models import OrderStatus

class ClientInfo(BaseModel):
    id: str
    email: str

class ProductInfo(BaseModel):
    id: str
    name: str
    price: float

class OrderCreate(BaseModel):
    client_id: str
    product_id: str
    quantity: Annotated[int, Field(strict=True, gt=0)]


class OrderOut(BaseModel):
    order_id: str
    client: ClientInfo
    product: ProductInfo
    quantity: int
    order_date: datetime
    total_value: float
    status: OrderStatus 
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class OrderDB(BaseModel):
    order_id: str
    client_id: str
    product_id: str
    quantity: int
    order_date: datetime
    total_value: float
    status: OrderStatus
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True