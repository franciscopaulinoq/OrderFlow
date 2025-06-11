import httpx
from fastapi import HTTPException

CLIENT_API_URL = "http://localhost:8001/api/v1/clients/"
PRODUCT_API_URL = "http://localhost:8000/api/v1/products/"

def validate_client(client_id: str):
    response = httpx.get(f"{CLIENT_API_URL}{client_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Client not found")

def get_product(product_id: str):
    response = httpx.get(f"{PRODUCT_API_URL}{product_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Product not found")
    return response.json()


def get_client(client_id: str):
    response = httpx.get(f"{CLIENT_API_URL}{client_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Client not found")
    return response.json()