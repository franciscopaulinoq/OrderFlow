import datetime
import uuid

from sqlalchemy.orm import Session

from . import models, schemas

def get_client(db: Session, client_id: str):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def get_clients(db: Session):
    return db.query(models.Client).all()

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(
        name=client.name, 
        email=client.email
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client