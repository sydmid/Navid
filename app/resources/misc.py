import pandas as pd
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sqlalchemy.ext.automap import automap_base

from app.tset_client import Downloader
from app.db import db


class DatabaseInit(Resource):
    @jwt_required()
    def post(self):
        Base = automap_base()
        Base.prepare(db.engine, reflect=True)
        inplace_tables = Base.classes
        downloader = Downloader()
        downloaded = downloader.initialize_existing_db()
        for key, value in downloaded.items():
            # stock_class = inplace_tables['stocks']
            # stock_dict = {'name': key, 'group': ''}
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
            # stock = stock_class(**stock_dict)
            # tables.append(stock)
            db.session.add_all(tables)
            db.session.commit()
