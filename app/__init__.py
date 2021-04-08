from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap

from config import config
from .main import db
from .main.utills import jwt_claim_handler, restful_api_resource_handler

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    api = Api(app)
    restful_api_resource_handler(api)

    jwt = JWTManager(app)
    jwt_claim_handler(jwt)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # @app.before_first_request
    # def create_tables():
    #     db.create_all()

    return app

