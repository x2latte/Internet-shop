from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = models.Order(user_id=order.user_id, total=0)
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