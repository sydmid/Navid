from app.db import StocksBase
from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from app.utils.stock_queries import date_functions

class خودرو(StocksBase):
    __tablename__ = 'خودرو'

    name = Column(String(15))
    group = Column(String(30))
    date = Column(Date, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    adjClose = Column(Float)
    value = Column(Integer)
    volume = Column(Integer)
    count = Column(Integer)
    close = Column(Float)
    individual_buy_count = Column(Integer)
    individual_sell_count = Column(Integer)
    individual_buy_vol = Column(Integer)
    individual_sell_vol = Column(Integer)
    individual_buy_value = Column(Integer)
    individual_sell_value = Column(Integer)
    corporate_buy_count = Column(Integer)
    corporate_sell_count = Column(Integer)
    corporate_buy_vol = Column(Integer)
    corporate_sell_vol = Column(Integer)
    corporate_buy_value = Column(Integer)
    corporate_sell_value = Column(Integer)
    individual_buy_mean_price = Column(Float)
    individual_sell_mean_price = Column(Float)
    corporate_buy_mean_price = Column(Float)
    corporate_sell_mean_price = Column(Float)
    individual_ownership_change = Column(Integer)
    jdate = Column(String)
    latin_name = Column(String)
    individual_buy_power = Column(Float)
    individual_sell_power = Column(Float)
    individual_buy_sell_ratio = Column(Float)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


