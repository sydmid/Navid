from flask_restful import Resource
from datetime import datetime, timedelta

from app.models.stock import *


class Stock(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, year_ago: int, name: str):
        time_span_ago = datetime.now() - timedelta(days=year_ago * 365)
        record = globals()[name].find_by_time_ago(time_span_ago)
        if not record:
            print("please check your Input Date")
        return {'thetyoe': f'{record}'}, 200
