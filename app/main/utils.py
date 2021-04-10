from flask import jsonify

from .resources.user import UserRegister, User, UserLogin, TokenRefresh, UserLogout
from .resources.stock import DBinit, Stock


def jwt_claim_handler(jwt):
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
        return jsonify(message=f"I'm sorry user with id:{jwt_payload['sub']} Your token is revoked plz Login again"), 401

    # in decrypted data u can access any data stored in a token
    # this can be the identity (comes from flask_jwt
    # _extended internals) and also the date token has been created and ...

    from .models.token import BlockedTokenModel

    @jwt.token_in_blocklist_loader
    def is_token_in_blocklist(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        token = BlockedTokenModel.find_by_jti(jti)
        return token is not None


def restful_api_resource_handler(api):
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user/<int:user_id>')
    api.add_resource(UserLogin, '/login')
    api.add_resource(TokenRefresh, '/refresh')
    api.add_resource(UserLogout, '/logout')
    api.add_resource(DBinit, '/stock')
    api.add_resource(Stock, '/stock/<string:name>')

