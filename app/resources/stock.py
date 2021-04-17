from flask_restful import Resource
from datetime import datetime

from app import db
from config import loadedTables


class Stock(Resource):
    loadedTables = loadedTables
    @classmethod
    # @jwt_required()
    def get(cls, name: str, from_date: str, to_date: str, step: int):
        global loadedTables
        from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
        to_date = datetime.strptime(to_date, "%Y-%m-%d").date()

        try:
            requested_stock = loadedTables[name]
        except:
            return {'message': 'Stock not found'}, 404
        records = db.session.query(requested_stock).filter\
                                  (requested_stock.date >= from_date,
                                   requested_stock.date <= to_date)
        returnobj = []
        for i in range(0, records.count(), step):
            returnobj.append(records[i])
        return [str([record.date,
                     record.open,
                     record.close,
                     record.value]) for record in returnobj]