from flask_restful import Resource

from config import _1_year_stocks, _2_year_stocks, _3_year_stocks, _5_year_stocks, _10_year_stocks, query_modes_object


yearrange = {1: _1_year_stocks,
             2: _2_year_stocks,
             3: _3_year_stocks,
             5: _5_year_stocks,
             10: _10_year_stocks}


class Stock(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, name: str, year_ago: int, mode: str):
        # from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
        global yearspans
        try:
            requested_stock = yearspans[year_ago][name]
        except:
            return {'message': 'Stock not found'}, 404

        return query_modes_object[mode](requested_stock)
