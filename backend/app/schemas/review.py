# Cтруктура данных для добавления отзывов на товары магазина

from pydantic import BaseModel

#   Эта схема гарантирует, что при отправке отзыва пользователем:
#   обязательно указана оценка (rating)
#   обязательно присутствует комментарий (comment)
#   данные имеют корректную структуру для записи в базу через ReviewService


class ReviewCreate(BaseModel):
    rating: int
    comment: str

