import datetime
import uuid

from sqlalchemy import Column, String, Float, DateTime
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)

    def __repr__(self):
        return f"<Product(id='{self.id}', name='{self.name}', price={self.price})>"