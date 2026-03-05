# Механизм аутентификации магазина

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from config.token import create_access_token

from config.database import get_db
from models.user_models import User

from config.hashing import Hashing

from sqlalchemy.orm import Session

#	отвечает за вход пользователя
# 	проверяет данные
# 	выдаёт токен доступа
# 	позволяет работать с личным кабинетом и заказами

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    if not Hashing.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )

    access_token = create_access_token(data={"sub": user.email})

    response = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "is_active": user.is_active,
        "jwtToken": access_token,
    }

    return response
