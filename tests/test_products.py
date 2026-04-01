# tests/test_products.py
import pytest

def test_create_product_unauthorized(client):
    response = client.post("/products/", json={
        "name": "Test Product",
        "description": "Test",
        "price": 100,
        "category_id": 1,
        "brand_id": 1
    })
    assert response.status_code == 401  # Требуется авторизация

def test_create_product_forbidden(client, auth_headers):
    response = client.post("/products/", json={
        "name": "Test Product",
        "description": "Test",
        "price": 100,
        "category_id": 1,
        "brand_id": 1
    }, headers=auth_headers)
    # Обычный пользователь не может создавать товары
    assert response.status_code == 403

def test_create_product_admin(client, admin_headers):
    # Сначала нужно создать категорию и бренд
    cat_resp = client.post("/categories/", json={"name": "Test Cat", "description": "Test"}, headers=admin_headers)
    assert cat_resp.status_code == 200
    cat_id = cat_resp.json()["id"]
    brand_resp = client.post("/brands/", json={"name": "Test Brand"}, headers=admin_headers)
    assert brand_resp.status_code == 200
    brand_id = brand_resp.json()["id"]
    
    response = client.post("/products/", json={
        "name": "Test Product",
        "description": "Test",
        "price": 100,
        "category_id": cat_id,
        "brand_id": brand_id
    }, headers=admin_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 100