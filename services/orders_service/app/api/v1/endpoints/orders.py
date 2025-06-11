from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from utils.validators import validate_client, get_product, get_client

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=schemas.OrderOut)
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    validate_client(order.client_id)

    product_data = get_product(order.product_id)
    unit_price = product_data["price"]

    total_value = unit_price * order.quantity

    db_order = models.Order(
        client_id=order.client_id,
        product_id=order.product_id,
        quantity=order.quantity,
        total_value=total_value
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=list[schemas.OrderDB])
def list_orders(db: Session = Depends(database.get_db)):
    return db.query(models.Order).all()

@router.get("/{order_id}", response_model=schemas.OrderOut)
def get_order(order_id: str, db: Session = Depends(database.get_db)):
    order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
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
    order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
