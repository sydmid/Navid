from flask import Blueprint
from flask_restful import Api

from app.resources.user import User, UserLogin, UserRegister, UserLogout, TokenRefresh
from app.resources.misc import DatabaseInit
from app.resources.stock import Stock

main = Blueprint('main', __name__)

api = Api(main)

api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(UserLogout, '/logout')
api.add_resource(DatabaseInit, '/dbinit')
api.add_resource(Stock, '/stock/<string:name>/<int:year_ago>/<string:mode>')