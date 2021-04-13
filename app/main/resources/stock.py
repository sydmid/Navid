from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from sqlalchemy.ext.automap import automap_base

from app.main import db

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

