# app/main.py

from fastapi import FastAPI
from app.routers import (
    products_router, categories_router, brands_router,
    images_router, auth_router, orders_router
)

app = FastAPI(
    title="E-Commerce API",
    description="API для управления товарами, категориями, брендами, изображениями и заказами",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(products_router)
app.include_router(categories_router)
app.include_router(brands_router)
app.include_router(images_router)
app.include_router(auth_router)
app.include_router(orders_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to E-Commerce API",
        "version": "2.0.0",
        "docs": "/docs"
    }

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)