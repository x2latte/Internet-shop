# Cтруктура базы данных для покупателей и администраторов интернет-магазина

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.database import Base

#   хранит данные пользователей магазина
#   управляет авторизацией и ролями
#   связывает пользователей с их отзывами

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String, default="user")
    is_active = Column(Boolean, default=False)

    reviews = relationship("ReviewModel", back_populates="user")

    def __repr__(self):
        return f"<User {self.email}"
