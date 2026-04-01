from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, Boolean, Enum, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import enum
from datetime import datetime

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    hashed_password = Column(String(200), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    is_active = Column(Boolean, default=True)

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    
    products = relationship("Product", back_populates="category")

class Brand(Base):
    __tablename__ = "brands"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    
    products = relationship("Product", back_populates="brand")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    brand_id = Column(Integer, ForeignKey("brands.id"), nullable=False)
    
    category = relationship("Category", back_populates="products")
    brand = relationship("Brand", back_populates="products")
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")

class ProductImage(Base):
    __tablename__ = "product_images"
    
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(500), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    
    product = relationship("Product", back_populates="images")

# Модель заказа
class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default="pending")  # pending, paid, shipped, delivered, cancelled
    total_price = Column(Float, default=0.0)
    
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

# Модель позиции заказа
class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_time = Column(Float, nullable=False)  # цена на момент заказа
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product")

# Добавляем связь в User
User.orders = relationship("Order", back_populates="user")