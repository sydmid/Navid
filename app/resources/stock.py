from flask_restful import Resource
from sqlalchemy.ext.automap import automap_base

from app import db

loadedTables = None


class Stock(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, name: str):
        global loadedTables
        if not loadedTables:
            base = automap_base()
            base.prepare(db.engine, reflect=True)
            loadedTables = base.classes
        try:
            requested_stock = loadedTables[name]
        except:
            return {'message': 'Stock not found'}, 404
        records = db.session.query(requested_stock).all()
        return [str(x.date) for x in records]

