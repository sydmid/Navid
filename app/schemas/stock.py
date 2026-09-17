from pydantic import BaseModel
from datetime import date
from typing import Optional

class StockChartSchema(BaseModel):
    date: date
    open: float
    close: float
    high: float
    low: float
    volume: int

    class Config:
        from_attributes = True

class StockGeneralSchema(BaseModel):
    date: date
    open: float
    adjClose: float
    volume: int
    high: float
    low: float
    count: int
    value: int
    close: float

    class Config:
        from_attributes = True

class StockClientsSchema(BaseModel):
    date: date
    individual_buy_count: Optional[int] = None
    individual_sell_count: Optional[int] = None
    individual_buy_vol: Optional[int] = None
    individual_sell_vol: Optional[int] = None
    individual_buy_value: Optional[int] = None
    individual_sell_value: Optional[int] = None
    corporate_buy_count: Optional[int] = None
    corporate_sell_count: Optional[int] = None
    corporate_buy_vol: Optional[int] = None
    corporate_sell_vol: Optional[int] = None
    corporate_buy_value: Optional[int] = None
    corporate_sell_value: Optional[int] = None
    individual_buy_mean_price: Optional[float] = None
    individual_sell_mean_price: Optional[float] = None
    corporate_buy_mean_price: Optional[float] = None
    corporate_sell_mean_price: Optional[float] = None
    individual_ownership_change: Optional[int] = None

    class Config:
        from_attributes = True

class StockAllSchema(BaseModel):
    date: date
    open: float
    adjClose: float
    volume: int
    high: float
    low: float
    count: int
    value: int
    close: float
    individual_buy_count: Optional[int] = None
    individual_sell_count: Optional[int] = None
    individual_buy_vol: Optional[int] = None
    individual_sell_vol: Optional[int] = None
    individual_buy_value: Optional[int] = None
    individual_sell_value: Optional[int] = None
    corporate_buy_count: Optional[int] = None
    corporate_sell_count: Optional[int] = None
    corporate_buy_vol: Optional[int] = None
    corporate_sell_vol: Optional[int] = None
    corporate_buy_value: Optional[int] = None
    corporate_sell_value: Optional[int] = None
    individual_buy_mean_price: Optional[float] = None
    individual_sell_mean_price: Optional[float] = None
    corporate_buy_mean_price: Optional[float] = None
    corporate_sell_mean_price: Optional[float] = None
    individual_ownership_change: Optional[int] = None

    class Config:
        from_attributes = True
