# Слой работы с базой данных интернет-магазина

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

#   dependency для FastAPI:
#   создаёт сессию БД
#   передаёт её в роут
#   автоматически закрывает после завершения запроса

# 	подключает backend к базе данных
#   управляет соединениями
#   позволяет выполнять запросы (поиск пользователя, создание заказа, добавление товара)


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()