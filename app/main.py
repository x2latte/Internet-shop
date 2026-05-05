# # app/main.py

# from fastapi import FastAPI
# from app.routers import (
#     products_router, categories_router, brands_router,
#     images_router, auth_router, orders_router
# )

# app = FastAPI(
#     title="E-Commerce API",
#     description="API для управления товарами, категориями, брендами, изображениями и заказами",
#     version="3.0.0",
#     docs_url="/docs",
#     redoc_url="/redoc"
# )

# app.include_router(products_router)
# app.include_router(categories_router)
# app.include_router(brands_router)
# app.include_router(images_router)
# app.include_router(auth_router)
# app.include_router(orders_router)

# @app.get("/")
# def root():
#     return {
#         "message": "Welcome to E-Commerce API",
#         "version": "2.0.0",
#         "docs": "/docs"
#     }

# # from fastapi.middleware.cors import CORSMiddleware
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["http://localhost:3000"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # ). from fastapi.middleware.cors import CORSMiddleware

# # app = FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["http://localhost:3000", "http://172.20.39.61:3000", "http://localhost:3000/login"],  
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# from fastapi.middleware.cors import CORSMiddleware

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000", "http://172.20.39.61:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.routers import (
    products_router, categories_router, brands_router,
    images_router, auth_router, orders_router
)
from fastapi.middleware.cors import CORSMiddleware
from app.websocket_manager import manager
from app.auth import get_current_user_ws

app = FastAPI(
    title="E-Commerce API",
    description="API для управления товарами, категориями, брендами, изображениями и заказами",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(products_router)
app.include_router(categories_router)
app.include_router(brands_router)
app.include_router(images_router)
app.include_router(auth_router)
app.include_router(orders_router)

origins = ["http://localhost:3000", "http://172.20.39.61:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Welcome to E-Commerce API",
        "version": "2.0.0",
        "docs": "/docs"
    }

@app.websocket("/ws/manager")
async def websocket_endpoint(websocket: WebSocket, token: str = None):
    if token is None:
        await websocket.close(code=1008)
        return
    try:
        user = await get_current_user_ws(token)
        if user.role not in ["manager", "admin"]:
            await websocket.close(code=1008)
            return
        await manager.connect(websocket)
        try:
            while True:
                await websocket.receive_text()
        except WebSocketDisconnect:
            manager.disconnect(websocket)
    except Exception:
        await websocket.close(code=1008)