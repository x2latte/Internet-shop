# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app
from app import models
import os

# Тестовая база данных (SQLite в памяти)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="session")
def db():
    # Создаем таблицы
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(db):
    with TestClient(app) as c:
        yield c

@pytest.fixture
def test_user(client):
    # Регистрация пользователя
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpass",
        "role": "user"
    })
    assert response.status_code == 200
    return response.json()

@pytest.fixture
def test_admin(client):
    response = client.post("/auth/register", json={
        "email": "admin@example.com",
        "username": "admin",
        "password": "adminpass",
        "role": "admin"
    })
    assert response.status_code == 200
    return response.json()

@pytest.fixture
def auth_headers(client, test_user):
    response = client.post("/auth/login", data={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def admin_headers(client, test_admin):
    response = client.post("/auth/login", data={"username": "admin", "password": "adminpass"})
    assert response.status_code == 200
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}