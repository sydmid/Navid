from fastapi import APIRouter

router = APIRouter()

from app.api.endpoints import user, stock

router.include_router(user.router, prefix="/user", tags=["User"])
router.include_router(stock.router, tags=["Stock"])
