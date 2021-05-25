from datetime import datetime, timedelta
from sqlalchemy.ext.automap import automap_base
from app.modes import general_data, clients_data, test_data
from app.db import db


loadedTables = {}

_1_year_span = {}
_2_year_span = {}
_3_year_span = {}
_5_year_span = {}
_10_year_span = {}

query_modes_object = {'general_data': general_data,
                      'clients_data': clients_data,
                      'test_data': test_data}


def _load_tables():
    base = automap_base()
    base.prepare(db.engine, reflect=True)
    global loadedTables
    for key, value in base.classes.items():
        loadedTables[key] = value


def _load_timespans():
    global loadedTables
    global _1_year_span
    global _2_year_span
    global _3_year_span
    global _5_year_span
    global _10_year_span

    year_span_stack = [_1_year_span,
                       _2_year_span,
                       _3_year_span,
                       _5_year_span,
                       _10_year_span]
    time_span_stack = [
        datetime.now() - timedelta(days=365),
        datetime.now() - timedelta(days=2 * 365),
        datetime.now() - timedelta(days=3 * 365),
        datetime.now() - timedelta(days=5 * 365),
        datetime.now() - timedelta(days=10 * 365)
    ]

    def _make_ready(ago):
        object_of_stocks = {}
        for stock in loadedTables.keys():
            # check if we are in one of the stock tables and not any other tables
            try:
                loadedTables[stock].date
            except:
                continue
            constrained_records = db.session.query(loadedTables[stock]).filter \
                (loadedTables[stock].date >= ago)
            object_of_stocks[stock] = constrained_records
        return object_of_stocks

    for i in range(5):
        for key, value in _make_ready(time_span_stack[i]).items():
            year_span_stack[i][key] = value
