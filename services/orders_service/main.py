from fastapi import FastAPI
from app.database import Base, engine
from app.api.v1.endpoints import orders, product_orders
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        
    allow_credentials=False,    
    allow_methods=["*"],        
    allow_headers=["*"],
)

app.include_router(orders.router)
app.include_router(product_orders.router)
