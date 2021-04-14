from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Float, Numeric, String, DateTime, Date, ForeignKey, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from .tset_client import Downloader
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///test.db')
metadata = MetaData()
downloader = Downloader(mode='test')


async def create_tset_tables():
    downloaded = await downloader.download()
    for key in downloaded.keys():
        records_table = type("Record", (Base,), {
            '__tablename__': f"{key}",
            'name': Column(String(15), ForeignKey('stocks.name')),
            'group': Column(String),
            'date': Column(Date, primary_key=True),
            'open': Column(Float),
            'high': Column(Float),
            'low': Column(Float),
            'adjClose': Column(Float),
            'value': Column(Integer),
            'volume': Column(Integer),
            'count': Column(Integer),
            'close': Column(Float),
            'individual_buy_count': Column(Integer),
            'individual_sell_count': Column(Integer),
            'individual_buy_vol': Column(Integer),
            'individual_sell_vol': Column(Integer),
            'individual_buy_value': Column(Integer),
            'individual_sell_value': Column(Integer),
            'corporate_buy_count': Column(Integer),
            'corporate_sell_count': Column(Integer),
            'corporate_buy_vol': Column(Integer),
            'corporate_sell_vol': Column(Integer),
            'corporate_buy_value': Column(Integer),
            'corporate_sell_value': Column(Integer),
            'individual_buy_mean_price': Column(Float),
            'individual_sell_mean_price': Column(Float),
            'corporate_buy_mean_price': Column(Float),
            'corporate_sell_mean_price': Column(Float),
            'individual_ownership_change': Column(Integer),
            'jdate': Column(String),

        })
    stocks_table = type("Stock", (Base,), {
        '__tablename__': "stocks",
        'name': Column(String(15), primary_key=True),
        'group': Column(String(15)),
        'records': relationship("Record")
    })
    Base.metadata.create_all(engine)


