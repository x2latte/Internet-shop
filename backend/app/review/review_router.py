# API для работы с отзывами, включая создание и просмотр отзывов на товары магазина

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.user_models import User
from schemas.review import ReviewCreate
from config.token import get_currentUser
from .review_service import ReviewService

# 	позволяет пользователям оставлять отзывы на товары
#   возвращает все отзывы для администрирования или анализа
#   защищает создание отзыва через JWT, чтобы только авторизованные пользователи могли оставлять отзывы

router = APIRouter(prefix="/review", tags=["Review"])

@router.get("/")
def getAllReview(db: Session = Depends(get_db)):
    return ReviewService.get_all(db=db)


@router.post("/create/{productid}")
def createReview(
    productid: int,
    request: ReviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_currentUser),
):
    print(request)
    print(productid)
    return ReviewService.create_review(
        request=request, productId=productid, db=db, current_user=current_user
    )


@router.post("/coba")
def cobaReview(request: ReviewCreate):
    return request

