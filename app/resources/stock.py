from flask_restful import Resource
from sqlalchemy.ext.automap import automap_base
from datetime import datetime

from app import db

loadedTables = None


class Stock(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, name: str, from_date: str, to_date: str, step: int):
        from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
        to_date = datetime.strptime(to_date, "%Y-%m-%d").date()

        global loadedTables
        if not loadedTables:
            base = automap_base()
            base.prepare(db.engine, reflect=True)
            loadedTables = base.classes
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