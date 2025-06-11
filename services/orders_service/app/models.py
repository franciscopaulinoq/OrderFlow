import uuid
import datetime
from enum import Enum
from sqlalchemy import( 
    Column, 
    DateTime, 
    Float, 
    String, 
    Integer,
)
from .database import Base  

class OrderStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Order(Base):
    __tablename__ = "orders"  

    order_id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    client_id = Column(String(36), nullable=False)  
    product_id = Column(String(36), nullable=False)  
    order_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    quantity = Column(Integer, nullable=False)  
    total_value = Column(Float, default=0.0)
    status = Column(String, default=OrderStatus.PENDING.value, nullable=False)  
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)