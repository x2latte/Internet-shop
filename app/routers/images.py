# app/routers/images.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app import database


router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ImageResponse)
def create_image(image: schemas.ImageCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == image.product_id).first()
    if not product:
        raise HTTPException(status_code=400, detail="Product not found")
    db_image = models.Image(url=image.url, product_id=image.product_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


@router.get("/", response_model=List[schemas.ImageResponse])
def get_images(db: Session = Depends(get_db)):
    return db.query(models.Image).all()

@router.put("/{image_id}", response_model=schemas.ImageResponse)
def update_image(image_id: int, image: schemas.ImageCreate, db: Session = Depends(get_db)):
    db_image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")

    db_image.url = image.url
    db.commit()
    db.refresh(db_image)
    return db_image


@router.delete("/{image_id}")
def delete_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    db.delete(image)
    db.commit()
    return {"message": "Image deleted"}