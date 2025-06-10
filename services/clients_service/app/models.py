from datetime import datetime
import uuid

from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Client(Base):
    __tablename__= "clients"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return f"<Client(id='{self.id}', name='{self.name}', email={self.email})>"