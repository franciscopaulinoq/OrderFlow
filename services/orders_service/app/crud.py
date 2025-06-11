from sqlalchemy.orm import Session

from .models import Order
from .schemas import OrderCreate, OrderOut

def get_order(
    db: Session,
    order_id: str
):
    return db.query(Order).filter(
        Order.order_id == order_id
    ).first()


def get_orders(
    db: Session
):
    return db.query(Order).all()

def create_order(
    db: Session,
    order: OrderCreate,
    total_value: float,
):
    db_order = Order(
        client_id=order.client_id,
        product_id=order.product_id,
        quantity=order.quantity,
        total_value=total_value
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: str):
    db_order = get_order(db, order_id)
    if db_order:
        db.delete(db_order)
        db.commit()
        return True
    return False