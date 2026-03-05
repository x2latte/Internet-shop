from pydantic import BaseModel
from typing import Optional

# Эта схема гарантирует корректность данных при:
#   создании нового аккаунта
#   определении роли пользователя (обычный пользователь или администратор)
#   хранении статуса активности для управления доступом


class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = "user"
    is_active: Optional[bool]
