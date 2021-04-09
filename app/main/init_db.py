from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Float, Numeric, String, DateTime, ForeignKey, create_engine)
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import asyncio
from tset_client import Downloader

Base = declarative_base()
engine = create_engine('sqlite:///test.db')
metadata = MetaData()
downloader = Downloader(mode='only_names')


async def init_db():
    downloaded = await downloader.download()
    for key in downloaded.keys():
        records_table = type("Record", (Base,), {
            '__tablename__': f"{key}",
            'name': Column(String(15), ForeignKey('stocks.name')),
            'date': Column(DateTime, primary_key=True),
            'open': Column(Float),
            'high': Column(Float),
            'low': Column(Float),
            'adjClose': Column(Float),
            'value': Column(Float),
            'volume': Column(Float),
            'count': Column(Float),
            'close': Column(Float),
        })
    stocks_table = type("Stock", (Base,), {
        '__tablename__': "stocks",
        'name': Column(String(15), primary_key=True),
        'group': Column(String(15)),
        'open': Column(Float),
        'high': Column(Float),
        'low': Column(Float),
        'adjClose': Column(Float),
        'value': Column(Float),
        'volume': Column(Float),
        'count': Column(Float),
        'close': Column(Float),
    })
    Base.metadata.create_all(engine)

asyncio.run(init_db())

