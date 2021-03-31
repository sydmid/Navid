from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_bootstrap import Bootstrap

from config import config
from .db import db
from .security import authenticate, identity
from .resources.user import UserRegister
from .resources.item import Item, ItemList
from .resources.store import Store, StoreList

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)

    api = Api(app)
    jwt = JWT(app, authenticate, identity)  # /auth

    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(StoreList, '/stores')
    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(UserRegister, '/register')

    @app.before_first_request
    def create_tables():
        db.create_all()

    db.init_app(app)
    return app

