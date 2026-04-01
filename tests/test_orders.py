# tests/test_orders.py
import pytest

def test_create_order_empty_cart(client, auth_headers):
    response = client.post("/orders/", json={"items": []}, headers=auth_headers)
    assert response.status_code == 400
    assert "Product" in response.json()["detail"]

def test_create_order_product_not_found(client, auth_headers):
    response = client.post("/orders/", json={"items": [{"product_id": 999, "quantity": 1}]}, headers=auth_headers)
    assert response.status_code == 400

def test_create_order_success(client, auth_headers):
    # Сначала создадим категорию, бренд, товар
    # (лучше вынести в фикстуры, но для краткости здесь)
    # Для упрощения создадим через API (требуется админ)
    # Мы можем использовать отдельную фикстуру с созданием товара, но для демонстрации:
    # Создадим товар через админский токен, но в тесте это может быть отдельно.
    # В реальном проекте лучше создать фикстуру product.
    pass  # Здесь нужно будет сначала создать товар, потом заказ.

def test_get_my_orders(client, auth_headers):
    response = client.get("/orders/", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)