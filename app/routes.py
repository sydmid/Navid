from flask import Blueprint
from flask_restful import Api

from app.resources.user import User, UserLogin, UserRegister, UserLogout, TokenRefresh
from app.resources.stock import StockYear, StockMonth, StockUtils, StockYearApi, StockMonthApi
from app.resources.stocks import StocksList
from app.resources.today_chart import StocksHistory
from app.resources.alternatives.db_initializer import DatabaseInit, DatabaseInitTest
from app.resources.alternatives.in_memory_stock_dict import MemoryStock

bp_rest = Blueprint('resources', __name__)

api = Api(bp_rest)

api.add_resource(UserRegister, '/register')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(User, '/user/<int:user_id>')
# s = span, y = year, m = month
api.add_resource(StockYear, '/stock-t-span/<string:name>/y/<int:year_ago>/<string:mode>')
api.add_resource(StockMonth, '/stock-t-span/<string:name>/m/<int:month_ago>/<string:mode>')
api.add_resource(StockYearApi, '/api/stock-t-span/<string:name>/y/<int:year_ago>/<string:mode>')
api.add_resource(StockMonthApi, '/api/stock-t-span/<string:name>/m/<int:month_ago>/<string:mode>')
api.add_resource(StocksList, '/stocks-list')
api.add_resource(StocksHistory, '/today/<string:name>')
api.add_resource(StockUtils, '/stock-utils')

# Alternatives
api.add_resource(DatabaseInit, '/dbinit')
api.add_resource(DatabaseInitTest, '/init-test')
api.add_resource(MemoryStock, '/imstock/<string:name>/<int:year_ago>/<string:mode>')
