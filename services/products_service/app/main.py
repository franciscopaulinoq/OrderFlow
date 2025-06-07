from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import Base, engine, get_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created/checked.")
    yield
    print("Shutting down Products Service.")


app = FastAPI(
    title="Products Service",
    description="API for managing product catalog.",
    version="0.0.1",
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {"message": "Welcome to Product Service!"}

@app.post("/products/", response_model=schemas.Product, status_code=status.HTTP_201_CREATED)
def create_product_endpoint(product: schemas.ProductBase, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=list[schemas.Product])
def read_products_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products