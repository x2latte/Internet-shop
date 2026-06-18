# clear_products.py
from app.database import SessionLocal
from app import models

db = SessionLocal()

# Удаляем изображения
db.query(models.ProductImage).delete()
# Удаляем товары
db.query(models.Product).delete()
# Удаляем категории
db.query(models.Category).delete()
# Удаляем бренды
db.query(models.Brand).delete()

db.commit()
db.close()
print("Все товары, категории, бренды и изображения удалены.")
