# app//schemas.py

from pydantic import BaseModel
from typing import List, Optional

# Пользователи
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = "user"

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    is_active: bool
    class Config:
        from_attributes = True

# Категории
class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = ""

class CategoryResponse(CategoryCreate):
    id: int
    class Config:
        from_attributes = True

# Бренды
class BrandCreate(BaseModel):
    name: str

class BrandResponse(BrandCreate):
    id: int
    class Config:
        from_attributes = True

# Продукты
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    count_in_stock: int
    category_id: int
    brand_id: int

class ProductResponse(ProductCreate):
    id: int
    category: CategoryResponse
    brand: BrandResponse
    images: List["ImageResponse"] = []
    class Config:
        from_attributes = True

# Изображения
class ImageCreate(BaseModel):
    url: str
    product_id: int

class ImageResponse(ImageCreate):
    id: int
    class Config:
        from_attributes = True

# Заказы
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderItemResponse(BaseModel):
    product: ProductResponse
    quantity: int
    price: float
    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderResponse(BaseModel):
    id: int
    user: UserResponse
    items: List[OrderItemResponse]
    total: float
    class Config:
        from_attributes = True