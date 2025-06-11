from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, crud, database
from utils.validators import validate_client, get_product, get_client

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=schemas.OrderDB)
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    validate_client(order.client_id)

    product_data = get_product(order.product_id)
    unit_price = product_data["price"]

    total_value = unit_price * order.quantity

    return crud.create_order(db, order, total_value)

@router.get("/", response_model=list[schemas.OrderDB])
def list_orders(db: Session = Depends(database.get_db)):
    return crud.get_orders(db)

@router.get("/{order_id}", response_model=schemas.OrderOut)
def get_order(order_id: str, db: Session = Depends(database.get_db)):
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    client_data = get_client(order.client_id)
    product_data = get_product(order.product_id)

    return schemas.OrderOut(
        order_id=order.order_id,
        client=schemas.ClientInfo(**client_data),
        product=schemas.ProductInfo(**product_data),
        quantity=order.quantity,
        order_date=order.order_date,  # <- você precisa garantir que esse campo existe no model
        total_value=order.total_value,
        status=order.status,
        created_at=order.created_at,
        updated_at=order.updated_at,
    )

@router.delete("/{order_id}", status_code=204)
def delete_order(order_id: str, db: Session = Depends(database.get_db)):
    success = crud.delete_order(db, order_id=order_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return