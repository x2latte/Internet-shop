# app/routers/__init__.py

from .products import router as products_router
from .categories import router as categories_router
from .brands import router as brands_router
from .images import router as images_router
from .auth import router as auth_router
from .orders import router as orders_router

__all__ = [
    "products_router", "categories_router", "brands_router",
    "images_router", "auth_router", "orders_router"
]