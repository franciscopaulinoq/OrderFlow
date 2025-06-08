from pydantic import BaseModel
from datetime import datetime

class ClientCreate(BaseModel):
    name: str
    email: str

class ClientOut(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True