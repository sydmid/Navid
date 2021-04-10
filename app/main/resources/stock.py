import pandas as pd
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from sqlalchemy.ext.automap import automap_base
from..models.stock import StockModel
from ..tset_client import Downloader
from app.main import db

Base = automap_base()


class DBinit(Resource):
    def get(self, name):
        item = StockModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self):
        Base.prepare(db.engine, reflect=True)
        inplace_tables = Base.classes
        downloader = Downloader()
        downloaded = downloader.initialize_existing_db()
        for key, value in downloaded.items():
            stock_class = inplace_tables['stocks']
            stock_dict = {'name': key, 'group': ''}
            record_class = inplace_tables[f"{key}"]
            tables = []
            record_dict = {'name': '', 'date': '',
                           'open': '', 'high': '',
                           'low': '', 'adjClose': '',
                           'value': '', 'volume': '',
                           'count': '', 'close': ''}
            df = pd.DataFrame(value)
            for row in df.itertuples():
                record_dict['name'] = key
                record_dict['date'] = row[0]
                record_dict['open'] = row[1]
                record_dict['high'] = row[2]
                record_dict['low'] = row[3]
                record_dict['adjClose'] = row[4]
                record_dict['value'] = row[5]
                record_dict['volume'] = row[6]
                record_dict['count'] = row[7]
                record_dict['close'] = row[8]
                record = record_class(**record_dict)
                tables.append(record)
            stock = stock_class(**stock_dict)
            tables.append(stock)
            db.session.add_all(tables)
            db.session.commit()


class Stock(Resource):
    def get(self, name):
        stock = StockModel.find_by_name(name)
        if stock:
            return stock.json()
        return {'message': 'Store not found'}, 404
