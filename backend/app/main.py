# Точка входа backend интернет-магазина, которая собирает все части системы и запускает API

import uvicorn

from fastapi import FastAPI
from config.database import engine
from config.database import Base
from auth import auth_router
from users import users_router
from review import review_router
from product import product_router
from order import order_router
from fastapi.middleware.cors import CORSMiddleware

### 1.	Создаёт сервер магазина
### Поднимает API на FastAPI.
###	2.	Подключает базу данных
### Создаёт таблицы для:
###	    пользователей
###		товаров
###		заказов
###		отзывов
###		авторизации
###	3.	Объединяет модули магазина
###	Подключает маршруты:
###		/api/login, /api/register
###		/api/users
###		/api/products
###		/api/orders
###		/api/reviews
###	4.	Разрешает запросы от фронтенда
###	Настраивает CORS, чтобы сайт мог обращаться к серверу.
###	5.	Запускает сервер
### Через uvicorn.

app = FastAPI(version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["Authorization"],
    allow_methods=["GET", "POST", "PUT", "DELETE"]
)


Base.metadata.create_all(bind=engine)


@app.get("/")
def hello():
    return "Backend ready (งツ)ว"


app.include_router(auth_router.router, prefix="/api")
app.include_router(users_router.router, prefix="/api")
app.include_router(review_router.router, prefix="/api")
app.include_router(product_router.router, prefix="/api")
app.include_router(order_router.router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
