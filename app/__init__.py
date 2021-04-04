from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap

from .main import db
from config import config
from .main.resources.user import UserRegister, User, UserLogin, TokenRefresh, UserLogout
from .main.resources.item import Item, ItemList
from .main.resources.store import Store, StoreList

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
    api.add_resource(UserLogout, '/logout')

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:  # Should be read from a config file or data base instead of hard coding
            return {'isAdmin': True}
        return {'isAdmin': False}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            'description': 'The token has expired',
            'error': 'token_expired'
        }), 401

    # when the token they send us in the Authorization Header is an Actual JWT (I.E its some random number)
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            'description': "I'm sorry Signature verification failed",
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
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return jsonify({
            'description': 'The token is not fresh',
            'error': 'fresh_token_required'
        }), 401

    # when the sign out and we don't want them to be able to use their last valid token anymore
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return jsonify(msg=f"I'm sorry {jwt_payload['sub']} I can't let you do that"), 401
    # in decrypted data u can access any data stored in a token
    # this can be the identity (comes from flask_jwt
    # _extended internals) and also the date token has been created and ...

    from .main.models.token import BlockedTokenModel

    @jwt.token_in_blocklist_loader
    def is_token_in_blocklist(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        token = BlockedTokenModel.find_by_jti(jti)
        return token is not None

    @app.before_first_request
    def create_tables():
        db.create_all()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    db.init_app(app)
    return app

