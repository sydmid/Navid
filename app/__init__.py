from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from config import config
from app.db import db
from app.jwt_callbacks import jwt_claim_handler
from app.resource_handling import restful_api_resource_handler


def create_app(config_name):
    app = Flask(__name__)
    load_dotenv(".env")

    app.config.from_object(config[config_name])
    # TODO implement Config.init_app
    config[config_name].init_app(app)

    db.init_app(app)

    api = Api(app)
    restful_api_resource_handler(api)

    jwt = JWTManager(app)
    jwt_claim_handler(jwt)

    @app.before_first_request
    def global_table_object_creator():
         db.create_all()

    @app.before_first_request
    def global_loaded_tables_creator():
        config['loadTables']()

    @app.before_first_request
    def global_stocks_timespan_data_creator():
        config['loadTimespans']()

    return app

