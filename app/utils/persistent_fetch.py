import collections

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from app.tset_client.tse_settings import TSE_ISNT_INFO_URL
from app.tset_client.download import download
from app.tset_client.ticker import Ticker
import json
import os
from concurrent import futures
from threading import Timer

ALL_INDEX_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/index_all.json'))

RealtimeTickerInfo = collections.namedtuple(
    'RealtimeTickerInfo', [
        'last_price',
        'adj_close',
        'best_demand_vol',
        'best_demand_price',
        'best_supply_vol',
        'best_supply_price',
    ]
)


def requests_retry_session(
        retries=10,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504, 503),
        session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def get_ticker_real_time_new(stock_id, session) -> RealtimeTickerInfo:
    # session = requests_retry_session()
    response = session.get(TSE_ISNT_INFO_URL.format(stock_id), timeout=10)
    # session.close()
    # check supply and demand data exists
    try:
        if response.text.split(";")[2] != "":
            best_demand_vol = int(response.text.split(";")[2].split("@")[1])
            best_demand_price = int(response.text.split(";")[2].split("@")[2])
            best_supply_vol = int(response.text.split(";")[2].split("@")[4])
            best_supply_price = int(response.text.split(";")[2].split("@")[3])
        else:
            best_demand_vol = None
            best_demand_price = None
            best_supply_vol = None
            best_supply_price = None
    except:
        'something bad has happened'

    # in some cases last price or adj price is undefined
    try:
        last_price = int(response.text.split()[1].split(",")[1])
    except (ValueError, IndexError):  # When instead of number value is `F`
        last_price = None
    try:
        adj_close = int(response.text.split()[1].split(",")[2])
    except (ValueError, IndexError):
        adj_close = None
    try:
        return RealtimeTickerInfo(
            last_price,
            adj_close,
            best_demand_vol=best_demand_vol,
            best_demand_price=best_demand_price,
            best_supply_vol=best_supply_vol,
            best_supply_price=best_supply_price,
        )
    except:
        return 'something is wrong'


def live_stock_fetcher():
    with open(ALL_INDEX_DIR, encoding="utf8", mode="r") as reader:
        loaded_json = json.loads(reader.read())
    df_list = {}
    future_to_symbol = {}
    printable = {}
    counter = 0
    with futures.ThreadPoolExecutor(max_workers=30) as executor:
        session = requests_retry_session()
        for i in loaded_json.keys():
            try:
                future = executor.submit(get_ticker_real_time_new, loaded_json[i], session)
                future_to_symbol[future] = i
                # print(f'sahme {i} ok bud')
            except:
                continue
                # print(f'sahme {i} moshkel darad')
        for future in futures.as_completed(future_to_symbol):
            printable[future_to_symbol[future]] = future.result()
        for x in printable.keys():
            if printable[x] == "something is wrong":
                print(x)
            # counter += 1
            # print(counter)
            # print(printable[x])

