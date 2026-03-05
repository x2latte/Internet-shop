# Pydantic-схемы для работы с заказами, включая адрес, корзину, пользователя и оплату

from pydantic import BaseModel
from typing import List

# 	валидируют входные данные API при создании заказа
#   обеспечивают корректность структуры: адрес, товары, пользователь, сумма
#   используются сервисом заказов (OrderService) и роутером /order

class CartSchema(BaseModel):
    address_line1: str
    address_city: str
    address_country: str
    address_zip: str


class TokenSchema(BaseModel):
    id: str
    email: str
    card: CartSchema


class CartItemSchema(BaseModel):
    name: str
    quantity: int
    price: int


class CurrentUserSchema(BaseModel):
    id: int
    name: str
    email: str
    role: str
    is_active: bool


class OrderCreatePlaceOrder(BaseModel):
    token: TokenSchema
    cartItems: List[CartItemSchema]
    currentUser: CurrentUserSchema
    subtotal: int

