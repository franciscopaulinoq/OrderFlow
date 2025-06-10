from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/product-orders", tags=["ProductOrders"])

@router.post("/", response_model=schemas.ProductOrderOut)
def create_product_order(product_order: schemas.ProductOrderCreate, db: Session = Depends(database.get_db)):
    db_po = models.ProductOrder(**product_order.dict())
    db.add(db_po)

    order = db.query(models.Order).filter(models.Order.order_id == product_order.order_id).first()

    if order:
        order.total_value = (order.total_value or 0) + (product_order.unit_price * product_order.quantity)
        db.add(order)

    db.commit()
    db.refresh(db_po)
    return db_po

@router.get("/", response_model=list[schemas.ProductOrderOut])
def list_product_orders(db: Session = Depends(database.get_db)):
    return db.query(models.ProductOrder).all()

@router.get("/{product_order_id}", response_model=schemas.ProductOrderOut)
def get_product_order(product_order_id: str, db: Session = Depends(database.get_db)):
    po = db.query(models.ProductOrder).filter(models.ProductOrder.product_order_id == product_order_id).first()
    if not po:
        raise HTTPException(status_code=404, detail="ProductOrder not found")
    return po

@router.delete("/{product_order_id}", status_code=204)
def delete_product_order(product_order_id: str, db: Session = Depends(database.get_db)):
    po = db.query(models.ProductOrder).filter(models.ProductOrder.product_order_id == product_order_id).first()
    if not po:
        raise HTTPException(status_code=404, detail="ProductOrder not found")
    db.delete(po)
    db.commit()
