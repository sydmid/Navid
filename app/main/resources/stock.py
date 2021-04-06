from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from ..models.record import Record
from..models.stock import StockModel
from ..tset_client import Downloader
import pandas as pd


class Stock(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #                     type=float,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    # parser.add_argument('store_id',
    #                     type=int,
    #                     required=True,
    #                     help="Every item needs a store_id."
    #                     )

    # @jwt_required()
    # def get(self, name):
    #     item = ItemModel.find_by_name(name)
    #     if item:
    #         return item.json()
    #     return {'message': 'Item not found'}, 404

    # @jwt_required(fresh=True)
    def post(self):
        downloader = Downloader()
        downloaded = downloader.update()
        for key, value in downloaded.items():
            isFirst = True
            stock = {'name': '', 'date': '',
                     'open': '', 'high': '',
                     'low': '', 'adjClose': '',
                     'value': '', 'volume': '',
                     'count': '', 'close': ''}
            df = pd.DataFrame(value)
            for index, row in df.iterrows():
                if isFirst:
                    stock['name'] = key
                    isFirst = False
                stock['date'] = index
                stock['open'] = row['open']
                stock['high'] = row['high']
                stock['low'] = row['low']
                stock['adjClose'] = row['adjClose']
                stock['value'] = row['value']
                stock['volume'] = row['volume']
                stock['count'] = row['count']
                stock['close'] = row['close']
                newrecord = Record(**stock)
                newrecord.save_to_db()
            try:
                return {'message': 'yes'}
            except:
                return {"message": "An error occurred inserting the item."}, 500

            stocks.append(stock)

#         if ItemModel.find_by_name(name):
#             return {'message': "An item with name '{}' already exists.".format(name)}, 400
#
#         data = Item.parser.parse_args()
#
#         item = ItemModel(name, **data)
#
#         try:
#             item.save_to_db()
#         except:
#             return {"message": "An error occurred inserting the item."}, 500
#
#         return item.json(), 201
#
#     @jwt_required()
#     def delete(self, name):
#         claims = get_jwt()
#         if not claims['isAdmin']:
#             return {'message': 'Admin privilege required'}, 401
#
#         item = ItemModel.find_by_name(name)
#         if item:
#             item.delete_from_db()
#             return {'message': 'Item deleted.'}
#         return {'message': 'Item not found.'}, 404
#
#     def put(self, name):
#         data = Item.parser.parse_args()
#
#         item = ItemModel.find_by_name(name)
#
#         if item:
#             item.price = data['price']
#         else:
#             item = ItemModel(name, **data)
#
#         item.save_to_db()
#
#         return item.json()
#
#
# class ItemList(Resource):
#     @jwt_required(optional=True)
#     def get(self):
#         user_id = get_jwt_identity()
#         items = [x.json() for x in ItemModel.find_all()]
#         if user_id:
#             return {'items': items}
#         return {'items': [x['name'] for x in items],
#                 'message': 'More Data would be available if u were Admin'}, 200
