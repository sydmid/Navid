import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from datetime import datetime, timedelta

from app.models.stocks import Stocks
from app.tset_client import Downloader
from app.db import db


class StocksList(Resource):
    @classmethod
    def get(cls):
        return Stocks.query_all_names()