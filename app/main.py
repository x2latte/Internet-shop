from fastapi import FastAPI
from app.routers import router as products_router
from app.routers import categories_router
from app.routers import brands_router
from app.routers import images_router
from app.routers import auth_router

app = FastAPI(
    title="E-Commerce API",
    description="API для управления товарами, категориями, брендами и изображениями",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Подключаем роутеры
app.include_router(products_router)
app.include_router(categories_router)
app.include_router(brands_router)
app.include_router(images_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to E-Commerce API",
        "version": "2.0.0",
        "docs": "/docs"
    }
