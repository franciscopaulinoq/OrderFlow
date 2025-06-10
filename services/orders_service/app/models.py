import uuid
import datetime
from enum import Enum
from sqlalchemy import( 
    Column, 
    DateTime, 
    Float, 
    String, 
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship
from .database import Base  

class OrderStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Order(Base):
    __tablename__ = "orders"  

    order_id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    client_id = Column(String(36), nullable=False)  
    order_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    total_value = Column(Float, default=0.0)
    status = Column(String, default=OrderStatus.PENDING.value, nullable=False)  
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)

    product_orders = relationship("ProductOrder", back_populates="order", cascade="all, delete-orphan")

class ProductOrder(Base):
    __tablename__ = "product_orders"  

    product_order_id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    order_id = Column(String(36), ForeignKey("orders.order_id"), nullable=False)  
    product_id = Column(String(36), nullable=False)  
    quantity = Column(Integer, nullable=False)  
    unit_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)

    order = relationship("Order", back_populates="product_orders")