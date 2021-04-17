from app.resources.user import User, UserLogin, UserRegister, UserLogout, TokenRefresh
from app.resources.misc import DatabaseInit
from app.resources.stock import Stock


def restful_api_resource_handler(api):
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user/<int:user_id>')
    api.add_resource(UserLogin, '/login')
    api.add_resource(TokenRefresh, '/refresh')
    api.add_resource(UserLogout, '/logout')
    api.add_resource(DatabaseInit, '/dbinit')
    api.add_resource(Stock, '/stock/<string:name>/<int:year_ago>/<string:mode>')