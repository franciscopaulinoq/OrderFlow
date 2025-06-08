from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Cliente(Base):
    __tablename__= "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    created_at = Column(DateTime, default=datetime.now)