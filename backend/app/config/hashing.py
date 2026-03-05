# Механизм хеширования и проверки паролей пользователей магазина

from passlib.context import CryptContext

#   защищает данные пользователей
#   не позволяет хранить пароли в открытом виде
#   предотвращает утечку реальных паролей при взломе базы

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hashing:
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)
