from contextlib import asynccontextmanager
from fastapi import FastAPI

from .database import Base, engine

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
)

@app.get("/")
async def root():
    return {"message": "Welcome to Product Service!"}