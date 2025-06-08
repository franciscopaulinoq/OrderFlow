from pydantic import BaseModel
from datetime import datetime

class ClienteCreate(BaseModel):
    nome: str
    email: str

class ClienteOut(BaseModel):
    id: int
    nome: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True