from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv

from config import config
from app.db import db
from app.jwt_callbacks import jwt_claim_handler
from app.resource_handling import restful_api_resource_handler

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    load_dotenv(".env")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    api = Api(app)
    restful_api_resource_handler(api)

    jwt = JWTManager(app)
    jwt_claim_handler(jwt)

    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    @app.before_first_request
    def global_table_object_creator():
         db.create_all()

    @app.before_first_request
    def load_tables():
        done = config['loadTables']()

    return app

