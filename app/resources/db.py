import pandas as pd
from datetime import datetime
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sqlalchemy.ext.automap import automap_base

from app.tset_client import Downloader
from app.db import db


class DatabaseInit(Resource):
    # @jwt_required()
    def post(self):
        Base = automap_base()
        Base.prepare(db.engine, reflect=True)
        inplace_tables = Base.classes
        # for the fetched data from resources to be merged as objects in all_stocks
        merged_stocks_object = {}
        # for counting and indexing clients data
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
                        # naming duplicates in each category differently by adding دو to them
                        if counted_stocks_1[f"{str(stockname).replace('ك', 'ک').replace('ي', 'ی').strip()}"]:
                            stockname = stockname + " دو"
                    except:
                        print('no duplicate')
                    stockname = str(stockname).replace('ك', 'ک').replace('ي', 'ی').strip()
                    merged_stocks_object[stockname] = []
                    df = pd.DataFrame(dataframe)
                    row_counter = 0
                    for row in df.itertuples():
                        merged_stocks_object[stockname].append({})
                        merged_stocks_object[stockname][row_counter]['name'] = stockname
                        merged_stocks_object[stockname][row_counter]['date'] = row.date
                        merged_stocks_object[stockname][row_counter]['open'] = row.open
                        merged_stocks_object[stockname][row_counter]['high'] = row.high
                        merged_stocks_object[stockname][row_counter]['low'] = row.low
                        merged_stocks_object[stockname][row_counter]['adjClose'] = row.adjClose
                        merged_stocks_object[stockname][row_counter]['value'] = row.value
                        merged_stocks_object[stockname][row_counter]['volume'] = row.volume
                        merged_stocks_object[stockname][row_counter]['count'] = row.count
                        merged_stocks_object[stockname][row_counter]['close'] = row.close
                        row_counter += 1
                    all_stock_rows[stockname] = row_counter
            elif download_category == 'download-clients':
                for stockname, dataframe in download_results.items():
                    try:
                        if counted_stocks_2[f"{str(stockname).replace('ك', 'ک').replace('ي', 'ی').strip()}"]:
                            stockname = stockname + " دو"
                    except:
                        print('no duplicate')
                    stockname = str(stockname).replace('ك', 'ک').replace('ي', 'ی').strip()
                    df = pd.DataFrame(dataframe)
                    row_counter = all_stock_rows[stockname] - 1
                    for row in df.itertuples():
                        merged_stocks_object[stockname][row_counter]['individual_buy_count'] = row.individual_buy_count
                        merged_stocks_object[stockname][row_counter]['individual_sell_count'] = row.individual_sell_count
                        merged_stocks_object[stockname][row_counter]['individual_buy_vol'] = row.individual_buy_vol
                        merged_stocks_object[stockname][row_counter]['individual_sell_vol'] = row.individual_sell_vol
                        merged_stocks_object[stockname][row_counter]['individual_buy_value'] = row.individual_buy_value
                        merged_stocks_object[stockname][row_counter]['individual_sell_value'] = row.individual_sell_value
                        merged_stocks_object[stockname][row_counter]['corporate_buy_count'] = row.corporate_buy_count
                        merged_stocks_object[stockname][row_counter]['corporate_sell_count'] = row.corporate_sell_count
                        merged_stocks_object[stockname][row_counter]['corporate_buy_vol'] = row.corporate_buy_vol
                        merged_stocks_object[stockname][row_counter]['corporate_sell_vol'] = row.corporate_sell_vol
                        merged_stocks_object[stockname][row_counter]['corporate_buy_value'] = row.corporate_buy_value
                        merged_stocks_object[stockname][row_counter]['corporate_sell_value'] = row.corporate_sell_value
                        merged_stocks_object[stockname][row_counter]['individual_buy_mean_price'] = row.individual_buy_mean_price
                        merged_stocks_object[stockname][row_counter]['individual_sell_mean_price'] = row.individual_sell_mean_price
                        merged_stocks_object[stockname][row_counter]['corporate_buy_mean_price'] = row.corporate_buy_mean_price
                        merged_stocks_object[stockname][row_counter]['corporate_sell_mean_price'] = row.corporate_sell_mean_price
                        merged_stocks_object[stockname][row_counter]['individual_ownership_change'] = row.individual_ownership_change
                        merged_stocks_object[stockname][row_counter]['jdate'] = str(row.jdate)
                        if row_counter != 0:
                            row_counter -= 1
        tables = []
        for stockname, stockrecords in merged_stocks_object.items():
            record_class = inplace_tables[f"{stockname}"]
            for record in stockrecords:
                tables.append(record_class(**record))
        db.session.add_all(tables)
        db.session.commit()

class DatabaseInitTest(Resource):
    def post(self):
        Base = automap_base()
        Base.prepare(db.engine, reflect=True)

        downloader = Downloader()
        downloaded = downloader.initialize_existing_db()

        for download_category, download_results in downloaded.items():
            if download_category == 'download-general':
                for stockname, dataframe in download_results.items():
                    df = pd.DataFrame(dataframe)
                    result = df.to_json(orient="split")
                    return result