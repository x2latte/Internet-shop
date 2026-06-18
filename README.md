# Интернет магазин  
**Направление подготовки:** 09.03.04 - Программная инженерия   
**Сроки прохождения практики:** 04.02.26 - 26.05.26  
**Руководитель практики:** ст. преподаватель В. М. Димитров 

Проект интеренет магазина на Fastapi и react с применением sqlalchemy, redux, and Postgresql

Магазин будет доступен по адресу: `http://localhost:8000/docs`

# Запуск интернет магазина:
lsof -ti:8000 | xargs kill -9 2>/dev/null
python -m uvicorn app.main:app --reload

# Запуск тестировки:
chmod +x test_all.sh
./test_all.sh

# frontend:
lsof -ti:3000 | xargs kill -9
cd admin-panel && npm start

# Посмотреть всех пользователей бд
sqlite3 ecommerce.db "SELECT * FROM users;"


# Деактивировать текущее окружение, если активно
deactivate

# Удалить старую папку venv
rm -rf venv

# Создать новое виртуальное окружение с python3.10 (или 3.11)
python3.10 -m venv venv
# Если нет python3.10, попробуйте python3.11 или просто python3 (но тогда проверьте версию)

# Активировать
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt

# Применить миграции
alembic upgrade head

# Создать админа
python create_admin.py   # или python3, если python недоступен

# Запустить сервер
uvicorn app.main:app --reload

cd "/Users/a1111/Documents/Ucheba/6 сем/Internet-shop"
source venv/bin/activate
python fill_db.py

cd "/Users/a1111/Documents/Ucheba/6 сем/Internet-shop"
source venv/bin/activate
rm -f ecommerce.db         
alembic upgrade head        
python create_admin.py      
python fill_db.py           