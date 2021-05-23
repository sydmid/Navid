from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Float, Numeric, String, DateTime, Date, ForeignKey, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from app.tset_client import Downloader
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///test.db')
metadata = MetaData()
downloader = Downloader(mode='production')


async def create_tset_tables():
    downloaded = await downloader.download()
    classes = {}
    for key in downloaded.keys():
        try:
            if classes[f"{str(key).replace('ك', 'ک').replace('ي', 'ی').strip()}"]:
                key = key + " دو"
        except:
            print('noDuplicateFound')
        classes[f"{str(key).replace('ك', 'ک').replace('ي', 'ی').strip()}"] = type("Record", (Base,), {
            '__tablename__': f"{str(key).replace('ك', 'ک').replace('ي', 'ی').strip()}",
            'name': Column(String(15)),
            'group': Column(String(30)),
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
    # classes['stocks'] = type("Stock", (Base,), {
    #     '__tablename__': "stocks",
    #     'name': Column(String(15), primary_key=True),
    #     'group': Column(String(15)),
    #     'records': relationship("Record")
    # })
    Base.metadata.create_all(engine)


