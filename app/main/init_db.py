from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, Float, Numeric, String, DateTime, ForeignKey, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from tset_client import Downloader
import pandas as pd

Base = declarative_base()
engine = create_engine('sqlite:///test.db')
metadata = MetaData()
downloader = Downloader()
downloaded = downloader.update()

for key in downloaded.keys():
    newTable = type("Record", (Base,), {
        '__tablename__': f"{key}",
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

Base.metadata.create_all(engine)
