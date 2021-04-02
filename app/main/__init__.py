from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap

from config import config
from .db import db
from .resources.user import UserRegister, User, UserLogin, TokenRefresh
from .resources.item import Item, ItemList
from .resources.store import Store, StoreList

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)

    api = Api(app)
    jwt = JWTManager(app)

    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(StoreList, '/stores')
    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user/<int:user_id>')
    api.add_resource(UserLogin, '/login')
    api.add_resource(TokenRefresh, '/refresh')

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:  # Should be read from a config file or data base instead of hard coding
            return {'isAdmin': True}
        return {'isAdmin': False}

    @app.before_first_request
    def create_tables():
        db.create_all()

    db.init_app(app)
    return app

