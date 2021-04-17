import pandas as pd
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sqlalchemy.ext.automap import automap_base

from app.models.stock import StockRecord
from app.tset_client import Downloader
from app.db import db


class DatabaseInit(Resource):
    # @jwt_required()
    def post(self):
        Base = automap_base()
        Base.prepare(db.engine, reflect=True)
        inplace_tables = Base.classes

        all_stocks = {}
        all_stock_rows = {}
        # for stock name duplicate handling
        counted_stocks_1 = {}
        counted_stocks_2 = {}


        downloader = Downloader()
        downloaded = downloader.initialize_existing_db()

        for download_category, download_results in downloaded.items():
            if download_category == 'download-general':
                for stockname, dataframe in download_results.items():
                    try:
                        if counted_stocks_1[f"{str(stockname).replace('ك', 'ک').replace('ي', 'ی').strip()}"]:
                            stockname = stockname + " دو"
                    except:
                        stockname = str(stockname).replace('ك', 'ک').replace('ي', 'ی').strip()
                    all_stocks[stockname] = []
                    df = pd.DataFrame(dataframe)
                    rowcounter = 0
                    for row in df.itertuples():
                        all_stocks[stockname].append({})
                        all_stocks[stockname][rowcounter]['name'] = stockname
                        all_stocks[stockname][rowcounter]['date'] = row[0]
                        all_stocks[stockname][rowcounter]['open'] = row.open
                        all_stocks[stockname][rowcounter]['high'] = row.high
                        all_stocks[stockname][rowcounter]['low'] = row.low
                        all_stocks[stockname][rowcounter]['adjClose'] = row.adjClose
                        all_stocks[stockname][rowcounter]['value'] = row.value
                        all_stocks[stockname][rowcounter]['volume'] = row.volume
                        all_stocks[stockname][rowcounter]['count'] = row.count
                        all_stocks[stockname][rowcounter]['close'] = row.close
                        rowcounter += 1
                    all_stock_rows[stockname] = rowcounter
            elif download_category == 'download-clients':
                for stockname, dataframe in download_results.items():
                    try:
                        if counted_stocks_2[f"{str(stockname).replace('ك', 'ک').replace('ي', 'ی').strip()}"]:
                            stockname = stockname + " دو"
                    except:
                        stockname = str(stockname).replace('ك', 'ک').replace('ي', 'ی').strip()
                    df = pd.DataFrame(dataframe)
                    rowcounter = all_stock_rows[stockname] - 1
                    for row in df.itertuples():
                        all_stocks[stockname][rowcounter]['individual_buy_count'] = row.individual_buy_count
                        all_stocks[stockname][rowcounter]['individual_sell_count'] = row.individual_sell_count
                        all_stocks[stockname][rowcounter]['individual_buy_vol'] = row.individual_buy_vol
                        all_stocks[stockname][rowcounter]['individual_sell_vol'] = row.individual_sell_vol
                        all_stocks[stockname][rowcounter]['individual_buy_value'] = row.individual_buy_value
                        all_stocks[stockname][rowcounter]['individual_sell_value'] = row.individual_sell_value
                        all_stocks[stockname][rowcounter]['corporate_buy_count'] = row.corporate_buy_count
                        all_stocks[stockname][rowcounter]['corporate_sell_count'] = row.corporate_sell_count
                        all_stocks[stockname][rowcounter]['corporate_buy_vol'] = row.corporate_buy_vol
                        all_stocks[stockname][rowcounter]['corporate_sell_vol'] = row.corporate_sell_vol
                        all_stocks[stockname][rowcounter]['corporate_buy_value'] = row.corporate_buy_value
                        all_stocks[stockname][rowcounter]['corporate_sell_value'] = row.corporate_sell_value
                        all_stocks[stockname][rowcounter]['individual_buy_mean_price'] = row.individual_buy_mean_price
                        all_stocks[stockname][rowcounter]['individual_sell_mean_price'] = row.individual_sell_mean_price
                        all_stocks[stockname][rowcounter]['corporate_buy_mean_price'] = row.corporate_buy_mean_price
                        all_stocks[stockname][rowcounter]['corporate_sell_mean_price'] = row.corporate_sell_mean_price
                        all_stocks[stockname][rowcounter]['individual_ownership_change'] = row.individual_ownership_change
                        all_stocks[stockname][rowcounter]['jdate'] = str(row.jdate)
                        if rowcounter != 0:
                            rowcounter -= 1
        tables = []
        for stockname, stockrecords in all_stocks.items():
            record_class = inplace_tables[f"{stockname}"]
            for record in stockrecords:
                tables.append(record_class(**record))
        db.session.add_all(tables)
        db.session.commit()
