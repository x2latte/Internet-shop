# Интернет магазин  
**Направление подготовки:** 09.03.04 - Программная инженерия   
**Сроки прохождения практики:** 04.02.26 - 26.05.26  
**Руководитель практики:** ст. преподаватель В. М. Димитров 

Проект интеренет магазина на Fastapi и react с применением sqlalchemy, redux, and Postgresql

Магазин будет доступен по адресу: `http://localhost:8000/docs`

Запуск интернет магазина:
lsof -ti:8000 | xargs kill -9 2>/dev/null
./venv/bin/uvicorn app.main:app --reload

Запуск тестировки:
chmod +x test_full.sh

frontend:
lsof -ti:3000 | xargs kill -9
cd admin-panel && npm start