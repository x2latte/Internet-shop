# app/routers/orders.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, models, auth
from app.database import get_db

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=schemas.Order)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    """Создать заказ (только для авторизованных пользователей)"""
    try:
        return crud.create_order(db, order, current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[schemas.Order])
def read_my_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    """Получить свои заказы"""
    orders = crud.get_orders_by_user(db, current_user.id, skip, limit)
    return orders

@router.get("/{order_id}", response_model=schemas.Order)
def read_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_active_user)
):
    """Получить детали заказа (только владелец или админ)"""
    if current_user.role == models.UserRole.ADMIN:
        order = crud.get_order(db, order_id)
    else:
        order = crud.get_order(db, order_id, current_user.id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# Эндпоинты для админов/менеджеров
@router.get("/admin/all", response_model=List[schemas.Order])
def read_all_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.check_manager_or_admin_role)
):
    """Получить все заказы (админ/менеджер)"""
    return crud.get_all_orders(db, skip, limit)

@router.put("/{order_id}/status", response_model=schemas.Order)
def update_order_status(
    order_id: int,
    status_update: schemas.OrderUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.check_manager_or_admin_role)
):
    """Обновить статус заказа (админ/менеджер)"""
    if not status_update.status:
        raise HTTPException(status_code=400, detail="Status is required")
    order = crud.update_order_status(db, order_id, status_update.status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.check_manager_or_admin_role)
):
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(order)
    db.commit()
    return {"message": "Order deleted successfully"}