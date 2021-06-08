from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv

from config import config
from app.utils import _load_tables, _load_timespans
from app.routes import bp_rest
from app.commands import bp_commands
from app.db import db
from app.utils import jwt_claim_handler

jwt = JWTManager()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)

    load_dotenv(".env")

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    migrate.init_app(app, db)

    db.init_app(app)
    app.register_blueprint(bp_commands)
    app.register_blueprint(bp_rest)

    @app.before_first_request
    def create_all_tables():
        db.create_all()

    # @app.before_first_request
    # def global_loaded_tables_creator():
    #     _load_tables()
    #
    # @app.before_first_request
    # def global_stocks_timespan_data_creator():
    #     _load_timespans()

    jwt.init_app(app)
    jwt_claim_handler(jwt)

    return app
