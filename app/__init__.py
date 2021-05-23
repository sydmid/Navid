from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv

from config import config
from app.utils.table_loader import _load_tables, _load_timespans
from app.views import main
from app.db import db
from app.jwt_callbacks import jwt_claim_handler
from app.models.stock import *

jwt = JWTManager()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)

    load_dotenv(".env")

    app.config.from_object(config[config_name])

    migrate.init_app(app, db)

    db.init_app(app)

    app.register_blueprint(main)

    jwt.init_app(app)
    jwt_claim_handler(jwt)

    # @app.before_first_request
    # def global_table_object_creator():
    #     db.create_all()

    @app.before_first_request
    def global_loaded_tables_creator():
        _load_tables()

    @app.before_first_request
    def global_stocks_timespan_data_creator():
        _load_timespans()

    return app

