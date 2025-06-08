from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)

@router.post("/", response_model=schemas.ClientOut)
def create_client_endpoint(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    """
    Cria um novo cliente.
    """
    return crud.create_client(db=db, client=client)

@router.get("/", response_model=list[schemas.ClientOut])
def read_clients_endpoint(db: Session = Depends(get_db)):
    """
    Retorna uma lista de clientes.
    """
    clients = crud.get_clients(db)
    return clients

@router.get("/{client_id}", response_model=schemas.ClientOut)
def read_client_endpoint(client_id, db: Session = Depends(get_db)):
    """
    Retorna um cliente específico pelo ID.
    """
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Client not found"
        )
    return db_client