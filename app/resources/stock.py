import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from datetime import datetime, timedelta

from app.models.stock import *
from app.tset_client import Downloader
from app.db import db


class StockYear(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, name: str, year_ago: int, mode: str):
        date = datetime.now() - timedelta(days=year_ago * 365)
        record = globals()[name].stock_from_date(date, mode)
        if not record:
            print("please check your Input Date")
        return {name: f'{record}'}, 200


class StockMonth(Resource):
    @classmethod
    # @jwt_required()
    def get(cls, name: str, month_ago: int, mode: str):
        date = datetime.now() - timedelta(days=month_ago * 30)
        records = globals()[name].stock_from_date(date, mode)
        if not records:
            print("We Cant Find The Time-Span you are requesting")
        return {name: f'{records}'}, 200


class StockUtils(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('stock_name',
                        action='append',
                        type=str,
                        required=True,
                        help="Stock name cannot be left blank!"
                        )
    parser.add_argument('job',
                        type=str,
                        required=True,
                        help="Job name cannot be left blank!"
                        )

    @classmethod
    def post(cls):
        posted_data = StockUtils.parser.parse_args()
        if posted_data['job'] == "full-update":
            downloader = Downloader()
            downloaded = downloader.update_existing_db()
            # for the fetched data from resources to be merged as objects in all_stocks
            merged_stocks_object = {}
            # for counting and indexing clients data
            all_stock_rows = {}
            # for stock name duplicate handling
            counted_stocks_1 = {}
            counted_stocks_2 = {}
            for download_category, download_results in downloaded.items():
                if download_category == 'download-general':
                    for stockname, dataframe in download_results.items():
                        try:
                            # naming duplicates in each category differently by adding دو to them
                            if counted_stocks_1[f"{str(stockname).replace('ك', 'ک').replace('ي', 'ی').strip()}"]:
                                stockname = stockname + " دو"
                        except:
                            pass
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
                            pass
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
                stockname = str.replace(stockname,' ','')
                record_class = globals()[stockname]
                try:
                    date = globals()[stockname].find_last_date()
                except:
                    date = None
                    print(f"cant find any current data for {stockname} in database")
                if date is not None:
                    existing_date = date
                    for record in stockrecords:
                        if record['date'] <= existing_date:
                            continue
                        tables.append(record_class(**record))
                else:
                    for record in stockrecords:
                        tables.append(record_class(**record))
            db.session.add_all(tables)
            db.session.commit()
        else:
            pass

        return {"message": f"{posted_data['job']} Done."}, 200
