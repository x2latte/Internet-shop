# Описание того, как интернет-магазин хранит заказы, товары в заказе и адрес доставки в базе данных

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Boolean, DateTime
from config.database import Base
from datetime import datetime

#   В контексте интернет-магазина
#   Когда пользователь оформляет заказ:
#   1.	Создаётся запись в order
#	2.	Сохраняется адрес в shipping
#	3.	Сохраняются товары в orderitems

#   Архитектурно
#   Это слой моделей БД. Он:
#	определяет структуру таблиц
#	используется SQLAlchemy
#	позволяет создавать и получать заказы из базы

class OrderModel(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    email = Column(String(30))
    orderAmount = Column(Integer)
    transactionId = Column(String)
    isDelivered = Column(Boolean)
    user_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class ShippingAddressModel(Base):
    __tablename__ = "shipping"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    postalCode = Column(Integer)
    country = Column(String)
    city = Column(String)
    order_id = Column(Integer)


class OrderItemsModel(Base):
    __tablename__ = "orderitems"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)
    order_id = Column(Integer)

