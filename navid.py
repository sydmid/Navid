import os
from app import create_app
from app.main.tset_client import Downloader


# downloader.update(mode="csv_download")
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.run(port=5000, debug=True)




# downloader = Downloader()
#         downloaded = downloader.update()
#         stocks = []
#         for key, value in downloaded.items():
#             isFirst = True
#             stock = {'name': '', 'date': [],
#                          'open': [], 'high': [],
#                          'low': [], 'adjClose': [],
#                          'value': [], 'volume': [],
#                          'count': [], 'close': []}
#             df = pd.DataFrame(value)
#             for index, row in df.iterrows():
#                 if isFirst:
#                     stock['name'] = key
#                     isFirst = False
#                 stock['date'].append(index)
#                 stock['open'].append(row['open'])
#                 stock['high'].append(row['high'])
#                 stock['low'].append(row['low'])
#                 stock['adjClose'].append(row['adjClose'])
#                 stock['value'].append(row['value'])
#                 stock['volume'].append(row['volume'])
#                 stock['count'].append(row['count'])
#                 stock['close'].append(row['close'])
#             newrecord = Record(**stock)
#             newrecord.save_to_db()
#             try:
#                 return {'message': 'yes'}
#             except:
#                 return {"message": "An error occurred inserting the item."}, 500
#
#             stocks.append(stock)
