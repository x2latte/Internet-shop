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