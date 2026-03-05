# Конфигурация интернет-магазина, файл глобальных настроек backend

import os
from dotenv import load_dotenv

load_dotenv()

# хранит параметры подключения к базе
# хранит секрет для токенов
# задаёт время жизни авторизации
# централизует конфигурацию проекта


class Settings:
    PROJECT_NAME: str = "Jojo Shops"
    PROJECT_VERSION: str = "1.0.0"
    USE_SQLITE_DB: str = "postgres"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD = "admin"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "postgres"
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = Settings()