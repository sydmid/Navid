from flask_restful import Resource

from config import _1_year_span, _2_year_span, _3_year_span, _5_year_span, _10_year_span, query_modes_object


yearrange = {1: _1_year_span,
             2: _2_year_span,
             3: _3_year_span,
             5: _5_year_span,
             10: _10_year_span}


class Stock(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, name: str, year_ago: int, mode: str):
        # from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
        global yearrange
        try:
            requested_stock = yearrange[year_ago][name]
        except:
            return {'message': 'Stock not found'}, 404

        return query_modes_object[mode](requested_stock)
