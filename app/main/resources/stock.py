from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from ..models.record import Record
from..models.stock import StockModel
from ..tset_client import Downloader
import pandas as pd
from app.main import db

class Stock(Resource):

    def post(self):
        downloader = Downloader()
        downloaded = downloader.update()
        for key, value in downloaded.items():
            override_dict = {'__tablename__': key}
            isFirst = True
            stock = {'name': '', 'date': '',
                     'open': '', 'high': '',
                     'low': '', 'adjClose': '',
                     'value': '', 'volume': '',
                     'count': '', 'close': ''}
            newRecord = type(f"{key}", (Record,), override_dict)
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
                newrecord = newRecord(**stock)
                db.session.add(newrecord)
                db.session.commmit()
                # newrecord.save_to_db()
