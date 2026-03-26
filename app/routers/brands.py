# app/routers/brands.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from typing import List
from app import database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.BrandResponse)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    db_brand = models.Brand(name=brand.name)
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


@router.get("/", response_model=List[schemas.BrandResponse])
def get_brands(db: Session = Depends(get_db)):
    return db.query(models.Brand).all()

@router.put("/{brand_id}", response_model=schemas.BrandResponse)
def update_brand(brand_id: int, brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    db_brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    if not db_brand:
        raise HTTPException(status_code=404, detail="Brand not found")

    db_brand.name = brand.name
    db.commit()
    db.refresh(db_brand)
    return db_brand


@router.delete("/{brand_id}")
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")

    db.delete(brand)
    db.commit()
    return {"message": "Brand deleted"}