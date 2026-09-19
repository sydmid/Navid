from fastapi import APIRouter

router = APIRouter()

from app.api.endpoints import user, stock
from app.api import websockets

router.include_router(user.router, prefix="/user", tags=["User"])
router.include_router(stock.router, tags=["Stock"])
router.include_router(websockets.router, prefix="/ws", tags=["Websockets"])
