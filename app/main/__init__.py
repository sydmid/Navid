from flask import Flask, jsonify
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

    @jwt.expired_token_loader
    def expired_token_callback():
        return jsonify({
            'description': 'The token has expired',
            'error': 'token_expired'
        }), 401

    # when the token they send us in the Authorization Header is an Actual JWT (I.E its some random number)
    @jwt.invalid_token_loader
    def expired_token_callback(error):
        return jsonify({
            'description': 'Signature verification failed',
            'error': 'invalid_token'
        }), 401

    # when they don't send us a JWT at all
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            'description': 'Request does not contain an access token',
            'error': 'authorization_required'
        }), 401

    # when they send us a non-fresh token but our endpoint requires fresh token (l.E our item post)
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback():
        return jsonify({
            'description': 'The token is not fresh',
            'error': 'fresh_token_required'
        }), 401

    # when the sign out and we don't want them to be able to use their last valid token anymore
    @jwt.revoked_token_loader
    def revoked_token_callback():
        return jsonify({
            'description': 'The token has been revoked',
            'error': 'token_revoked'
        }), 401

    @app.before_first_request
    def create_tables():
        db.create_all()

    db.init_app(app)
    return app

