from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
import enum

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class Category(CategoryBase):
    id: int
    class Config:
        from_attributes = True

class BrandBase(BaseModel):
    name: str

class BrandCreate(BrandBase):
    pass

class BrandUpdate(BaseModel):
    name: Optional[str] = None

class Brand(BrandBase):
    id: int
    class Config:
        from_attributes = True

class ProductImageBase(BaseModel):
    image_url: str

class ProductImageCreate(ProductImageBase):
    pass

class ProductImage(ProductImageBase):
    id: int
    product_id: int
    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int
    brand_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None
    brand_id: Optional[int] = None

class Product(ProductBase):
    id: int
    category: Category
    brand: Brand
    images: List[ProductImage] = []
    class Config:
        from_attributes = True

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

class UserBase(BaseModel):
    email: EmailStr
    username: str
    role: UserRole = UserRole.USER

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: int
    is_active: bool
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class LoginRequest(BaseModel):
    username: str
    password: str

# OrderItem
class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    order_id: int
    price_at_time: float
    product: Product
    class Config:
        from_attributes = True

class OrderBase(BaseModel):
    pass

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]  # список товаров с количеством

class OrderUpdate(BaseModel):
    status: Optional[str] = None

class Order(OrderBase):
    id: int
    user_id: int
    created_at: datetime
    status: str
    total_price: float
    items: List[OrderItem] = []
    user: User
    class Config:
        from_attributes = True