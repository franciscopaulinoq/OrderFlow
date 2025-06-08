from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)

@router.post("/", response_model=schemas.ClientOut)
def create_client_endpoint(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    """
    Cria um novo cliente.
    """
    db_client = models.Client(
        name=client.name, 
        email=client.email
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.get("/", response_model=list[schemas.ClientOut])
def read_clients_endpoint(db: Session = Depends(get_db)):
    """
    Retorna uma lista de clientes.
    """
    return db.query(models.Client).all()