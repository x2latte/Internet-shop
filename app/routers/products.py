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


@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == product.category_id).first()
    brand = db.query(models.Brand).filter(models.Brand.id == product.brand_id).first()
    if not category or not brand:
        raise HTTPException(status_code=400, detail="Category or Brand not found")
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        count_in_stock=product.count_in_stock,
        category_id=product.category_id,
        brand_id=product.brand_id,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/", response_model=List[schemas.ProductResponse])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Product).offset(skip).limit(limit).all()