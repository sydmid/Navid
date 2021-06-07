import pandas as pd
from flask import request
from flask_restful import Resource, reqparse
from datetime import datetime, timedelta

from app.models.today import *
from app.tset_client import Downloader
from app.db import db


class StocksHistory(Resource):
    @classmethod
    def get(cls, name: str):
        record = globals()[name].query_all()
        if not record:
            print("Could not find any data for today")
        return {name: f'{record}'}, 200