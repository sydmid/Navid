from app.db import db
from config import loadedTables
from datetime import datetime, timedelta

_1_year_stocks = {}
_2_year_stocks = {}
_3_year_stocks = {}
_5_year_stocks = {}
_10_year_stocks = {}


def ready():
    global loadedTables
    global _1_year_stocks
    global _2_year_stocks
    global _3_year_stocks
    global _5_year_stocks
    global _10_year_stocks

    stock_year_stack = [_1_year_stocks,
                        _2_year_stocks,
                        _3_year_stocks,
                        _5_year_stocks,
                        _10_year_stocks]

    _1year_ago = datetime.now() - timedelta(days=365)
    _2year_ago = datetime.now() - timedelta(days=2*365)
    _3year_ago = datetime.now() - timedelta(days=3*365)
    _5year_ago = datetime.now() - timedelta(days=5*365)
    _10year_ago = datetime.now() - timedelta(days=10*365)

    time_span_stack = [_1year_ago,
                       _2year_ago,
                       _3year_ago,
                       _5year_ago,
                       _10year_ago]

    def _make_ready(ago):
        object_of_stocks = {}
        for stock in loadedTables.keys():
            # check if we are in one of the stock tables and not any other tables
            try:
                loadedTables[stock].date
            except:
                continue
            records = db.session.query(loadedTables[stock]).filter \
                (loadedTables[stock].date >= ago)
            object_of_stocks[stock] = records
        return object_of_stocks

    for i in range(5):
        for key, value in _make_ready(time_span_stack[i]).items():
            stock_year_stack[i][key] = value
