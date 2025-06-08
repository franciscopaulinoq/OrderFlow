from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
import models
import schemas

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created/checked.")
    yield
    print("Shutting down Clients Service.")

app = FastAPI(
    title="Clients Service",
    description="API for managing clients.",
    version="0.0.1",
    lifespan=lifespan,
)

@app.post("/clients", response_model=schemas.ClientOut)
def create_client_endpoint(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_cliente = models.Client(name=client.name, email=client.email)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@app.get("/clients", response_model=list[schemas.ClientOut])
def read_clients_endpoint(db: Session = Depends(get_db)):
    return db.query(models.Client).all()

