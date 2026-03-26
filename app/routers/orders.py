# app/routers/orders.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, auth
from fastapi.security import OAuth2PasswordBearer
from app import database

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    payload = auth.jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
    user_id = payload.get("sub")
    
    db_order = models.Order(user_id=user_id, total=0)
    db.add(db_order)
    total = 0
    for item in order.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=400, detail=f"Product {item.product_id} not found")
        db_item = models.OrderItem(
            order=db_order,
            product=product,
            quantity=item.quantity,
            price=product.price
        )
        db.add(db_item)
        total += product.price * item.quantity
    db_order.total = total
    db.commit()
    db.refresh(db_order)
    return db_order


@router.get("/", response_model=List[schemas.OrderResponse])
def get_orders(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    payload = auth.jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
    if payload.get("role") not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not authorized")
    return db.query(models.Order).all()