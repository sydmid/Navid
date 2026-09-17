from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator
from app.core.config import settings

# Default engine
engine = create_engine(settings.DEV_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Bind engines for different databases
stocks_dict_engine = create_engine(settings.SQLALCHEMY_BINDS['stocks_dict'], connect_args={"check_same_thread": False})
today_chart_engine = create_engine(settings.SQLALCHEMY_BINDS['today_chart'], connect_args={"check_same_thread": False})

StocksDictSession = sessionmaker(autocommit=False, autoflush=False, bind=stocks_dict_engine)
TodayChartSession = sessionmaker(autocommit=False, autoflush=False, bind=today_chart_engine)

Base = declarative_base()
StocksBase = declarative_base()
TodayBase = declarative_base()

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_stocks_db() -> Generator:
    try:
        db = StocksDictSession()
        yield db
    finally:
        db.close()

def get_today_chart_db() -> Generator:
    try:
        db = TodayChartSession()
        yield db
    finally:
        db.close()
