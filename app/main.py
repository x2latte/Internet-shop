# app/main.py

from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, products, categories, brands, images, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Internet Shop API", version="0.1.0")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(brands.router, prefix="/brands", tags=["Brands"])
app.include_router(images.router, prefix="/images", tags=["Images"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])