from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, models
from app.database import get_db

router = APIRouter(prefix="/images", tags=["Images"])

@router.post("/", response_model=schemas.ProductImage)
def create_image(
    image: schemas.ProductImageCreate,
    product_id: int = Query(..., description="ID товара, к которому добавляется изображение"),
    db: Session = Depends(get_db)
):
    """Добавить изображение к товару"""
    # Проверяем, существует ли товар
    product = crud.get_product(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.create_image(db=db, image=image, product_id=product_id)

@router.get("/product/{product_id}", response_model=List[schemas.ProductImage])
def read_images_by_product(product_id: int, db: Session = Depends(get_db)):
    """Получить все изображения товара"""
    # Проверяем, существует ли товар
    product = crud.get_product(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.get_images_by_product(db, product_id=product_id)

@router.get("/", response_model=List[schemas.ProductImage])
def read_all_images(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Получить список всех изображений (с пагинацией)"""
    # Для простоты вернем все изображения с пагинацией
    # В реальном проекте может понадобиться отдельный метод в CRUD
    images = db.query(models.ProductImage).offset(skip).limit(limit).all()
    return images

@router.put("/{image_id}", response_model=schemas.ProductImage)
def update_image(
    image_id: int,
    image_update: schemas.ProductImageCreate,
    db: Session = Depends(get_db)
):
    """Обновить URL изображения"""
    db_image = crud.get_image(db, image_id=image_id)
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    db_image.image_url = image_update.image_url
    db.commit()
    db.refresh(db_image)
    return db_image

@router.delete("/{image_id}")
def delete_image(image_id: int, db: Session = Depends(get_db)):
    """Удалить изображение"""
    success = crud.delete_image(db, image_id=image_id)
    if not success:
        raise HTTPException(status_code=404, detail="Image not found")
    return {"message": "Image deleted successfully"}
