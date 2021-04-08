import pandas as pd
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from sqlalchemy.ext.automap import automap_base
from..models.stock import StockModel
from ..tset_client import Downloader
from app.main import db

Base = automap_base()

class Stock(Resource):
    def post(self):
        Base.prepare(db.engine, reflect=True)
        inplace_tables = Base.classes
        downloader = Downloader()
        downloaded = downloader.update()
        for key, value in downloaded.items():
            table = inplace_tables[f"{key}"]
            tables = []
            stock = {'date': '',
                     'open': '', 'high': '',
                     'low': '', 'adjClose': '',
                     'value': '', 'volume': '',
                     'count': '', 'close': ''}
            df = pd.DataFrame(value)
            for row in df.itertuples():
                stock['date'] = row[0]
                stock['open'] = row[1]
                stock['high'] = row[2]
                stock['low'] = row[3]
                stock['adjClose'] = row[4]
                stock['value'] = row[5]
                stock['volume'] = row[6]
                stock['count'] = row[7]
                stock['close'] = row[8]
                record = table(**stock)
                tables.append(record)
            db.session.add_all(tables)
            db.session.commit()

