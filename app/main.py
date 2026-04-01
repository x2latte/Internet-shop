from fastapi import FastAPI
from app.routers import products, categories, brands, images

app = FastAPI(
    title="E-Commerce API",
    description="API для управления товарами, категориями, брендами и изображениями",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Исправлено: products, categories и т.д. уже являются роутерами
app.include_router(products)
app.include_router(categories)
app.include_router(brands)
app.include_router(images)

@app.get("/")
def root():
    return {"message": "Welcome to E-Commerce API"}
