from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as api_router
from app.db import engine, stocks_dict_engine, today_chart_engine
from app.db import Base, StocksBase, TodayBase
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(title="Navid API", version="1.0.0", debug=settings.DEBUG)

    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    # Create tables on startup, binding correctly to their respective bases
    @app.on_event("startup")
    def on_startup():
        Base.metadata.create_all(bind=engine)
        StocksBase.metadata.create_all(bind=stocks_dict_engine)
        TodayBase.metadata.create_all(bind=today_chart_engine)

    return app

app = create_app()
