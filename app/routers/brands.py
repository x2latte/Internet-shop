from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/brands", tags=["Brands"])

@router.post("/", response_model=schemas.Brand)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    """Создать новый бренд"""
    return crud.create_brand(db=db, brand=brand)

@router.get("/", response_model=List[schemas.Brand])
def read_brands(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """Получить список всех брендов"""
    brands = crud.get_brands(db, skip=skip, limit=limit)
    return brands

@router.get("/{brand_id}", response_model=schemas.Brand)
def read_brand(brand_id: int, db: Session = Depends(get_db)):
    """Получить информацию о конкретном бренде"""
    db_brand = crud.get_brand(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand

@router.put("/{brand_id}", response_model=schemas.Brand)
def update_brand(
    brand_id: int, 
    brand_update: schemas.BrandUpdate, 
    db: Session = Depends(get_db)
):
    """Обновить информацию о бренде"""
    db_brand = crud.update_brand(db, brand_id=brand_id, brand_update=brand_update)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand

@router.delete("/{brand_id}")
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    """Удалить бренд"""
    success = crud.delete_brand(db, brand_id=brand_id)
    if not success:
        raise HTTPException(status_code=404, detail="Brand not found")
    return {"message": "Brand deleted successfully"}
