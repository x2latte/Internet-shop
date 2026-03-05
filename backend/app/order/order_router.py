# API для работы с заказами в магазине: CRUD + экспорт данных

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from starlette.responses import StreamingResponse
from config.database import get_db
from schemas.order import OrderCreatePlaceOrder
from .order_service import OrderService

# 	управляет заказами: просмотр, создание, удаление
#   позволяет администратору экспортировать все заказы в CSV для отчётов
#   использует сервис OrderService, чтобы вынести бизнес-логику из роутера

router = APIRouter(prefix="/order", tags=["Order"])

@router.get("/")
def getAll(db: Session = Depends(get_db)):
    return OrderService.getAll(db=db)


@router.post("/")
def createOrder(request: OrderCreatePlaceOrder, db: Session = Depends(get_db)):
    return OrderService.createOrderPlace(request=request, db=db)


@router.get("/orderbyuser/{userid}")
def orderByUser(userid: int, db: Session = Depends(get_db)):
    return OrderService.getOrderByUserId(userid=userid, db=db)


@router.get("/orderbyid/{id}")
def orderById(id: int, db: Session = Depends(get_db)):
    return OrderService.getOrderById(id=id, db=db)


@router.delete("/orderbyid/{id}")
def deleteById(orderid: int, db: Session = Depends(get_db)):
    return OrderService.deleteOrderById(orderid=orderid, db=db)

@router.get("/export-csv")
def export_csv(db: Session = Depends(get_db)):
    orders = OrderService.getAll(db=db)
    csv_data = "OrderID,Product,Quantity,Price,Name,Email,TransactionId,UserId,Id,IsDelivered\n"
    for order in orders:
        csv_data += f"{order.id},{order.name},{order.orderAmount},{order.price},"
        csv_data += f"{order.name},{order.email},{order.transactionId},{order.user_id},{order.id},{order.isDelivered}\n"

    response = StreamingResponse(content=iter([csv_data]), media_type="text/csv")
    response.headers["Content-Disposition"] = 'attachment; filename="orders.csv"'

    return response
