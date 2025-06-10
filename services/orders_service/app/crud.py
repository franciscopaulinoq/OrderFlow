from sqlalchemy.orm import Session

from .models import Order, ProductOrder
from .schemas import OrderCreate, OrderOut, ProductOrderCreate, ProductOrderOut

def get_order(
    db: Session,
    order_id: str
):
    return db.query(Order).filter(
        Order.order_id == order_id
    ).first


def get_orders(
    db: Session
):
    return db.query(Order).all()

def create_order(
    db: Session,
    order_data: OrderCreate
):
    new_order = Order(
        client_id=order_data.client_id,
        total_value=order_data.total_value
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order