import os
from datetime import timedelta
from sqlalchemy.ext.automap import automap_base
from datetime import datetime, timedelta

from app.db import db
from app.modes import general_data, clients_data, test_data

basedir = os.path.abspath(os.path.dirname(__file__))

loadedTables = {}

_1_year_stocks = {}
_2_year_stocks = {}
_3_year_stocks = {}
_5_year_stocks = {}
_10_year_stocks = {}

query_modes_object = {'general_data': general_data,
                      'clients_data': clients_data,
                      'test_data': test_data}


class Config:
    toBeContinued = True

    @staticmethod
    def init_app(app):
        pass


class PreAlphaConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jose'
    DOWNLOAD_DIR = os.path.join(basedir, 'download')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test.db') + '?check_same_thread=False'
    # 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    # disables the flask_sqlachemy track modification not sqlalchemy itself
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # flask extensions like flask_jwt can raise their own exception and app will know their specific error
    PROPAGATE_EXCEPTIONS = True
    # We choose it to be different than app.secret_key (Optional)
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or \
        'mysecret1'
    # Black list is disabled by default
    # Dont need it in flask 4
    # JWT_BLACKLIST_ENABLED = True
    # Enable The Black List for both access and refresh token
    # Dont need it in flask 4
    # JWT_BLACKLIST_TOKEN_CHECKS = ['access', ' refresh']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


def _load_tables():
    base = automap_base()
    base.prepare(db.engine, reflect=True)
    global loadedTables
    for key, value in base.classes.items():
        loadedTables[key] = value


def _load_timespans():
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
    _2year_ago = datetime.now() - timedelta(days=2 * 365)
    _3year_ago = datetime.now() - timedelta(days=3 * 365)
    _5year_ago = datetime.now() - timedelta(days=5 * 365)
    _10year_ago = datetime.now() - timedelta(days=10 * 365)

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


config = {
    'development': PreAlphaConfig,
    'testing': PreAlphaConfig,
    'production': PreAlphaConfig,
    'default': PreAlphaConfig,
    'loadTables': _load_tables,
    'loadTimespans': _load_timespans
}




