# Pydantic-схемы для API товаров и отзывов, обеспечивающие корректность данных магазина

from pydantic import BaseModel
from typing import Optional

# 	валидируют входные данные для товаров и отзывов
#   гарантируют, что все обязательные поля присутствуют
#   позволяют сервисам (ProductService, ReviewService) и роутерам работать с корректными структурами данных

class ReviewSchema(BaseModel):
    user_id: int
    name: str
    comment: str
    rating: int


class ProductSchema(BaseModel):
    name: str
    image: str
    category: str
    description: str
    price: int
    countInStock: int
    rating: Optional[int]
