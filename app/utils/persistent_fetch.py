import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from app.tset_client.tse_settings import TSE_ISNT_INFO_URL
import json
import os
from concurrent import futures


ALL_INDEX_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/index_all.json'))
res_lambda_dict = {
    "best_demand_vol": lambda x: int(x.split(";")[2].split("@")[1]),
    "best_demand_vol2": lambda x: int(x.split(";")[2].split("@")[6]),
    "best_demand_vol3": lambda x: int(x.split(";")[2].split("@")[11]),
    "best_demand_vol4": lambda x: int(x.split(";")[2].split("@")[16]),
    "best_demand_vol5": lambda x: int(x.split(";")[2].split("@")[21]),
    "best_demand_price": lambda x: int(x.split(";")[2].split("@")[2]),
    "best_demand_price2": lambda x: int(x.split(";")[2].split("@")[7]),
    "best_demand_price3": lambda x: int(x.split(";")[2].split("@")[12]),
    "best_demand_price4": lambda x: int(x.split(";")[2].split("@")[17]),
    "best_demand_price5": lambda x: int(x.split(";")[2].split("@")[22]),
    "best_demand_num": lambda x: int(x.split(";")[2].split("@")[0]),
    "best_demand_num2": lambda x: int(x.split(";")[2].split("@")[5].split(",")[1]),
    "best_demand_num3": lambda x: int(x.split(";")[2].split("@")[10].split(",")[1]),
    "best_demand_num4": lambda x: int(x.split(";")[2].split("@")[15].split(",")[1]),
    "best_demand_num5": lambda x: int(x.split(";")[2].split("@")[20].split(",")[1]),
    "best_supply_vol": lambda x: int(x.split(";")[2].split("@")[4]),
    "best_supply_vol2": lambda x: int(x.split(";")[2].split("@")[9]),
    "best_supply_vol3": lambda x: int(x.split(";")[2].split("@")[14]),
    "best_supply_vol4": lambda x: int(x.split(";")[2].split("@")[19]),
    "best_supply_vol5": lambda x: int(x.split(";")[2].split("@")[24]),
    "best_supply_price": lambda x: int(x.split(";")[2].split("@")[3]),
    "best_supply_price2": lambda x: int(x.split(";")[2].split("@")[8]),
    "best_supply_price3": lambda x: int(x.split(";")[2].split("@")[13]),
    "best_supply_price4": lambda x: int(x.split(";")[2].split("@")[18]),
    "best_supply_price5": lambda x: int(x.split(";")[2].split("@")[23]),
    "best_supply_num": lambda x: int(x.split(";")[2].split("@")[5].split(",")[0]),
    "best_supply_num2": lambda x: int(x.split(";")[2].split("@")[10].split(",")[0]),
    "best_supply_num3": lambda x: int(x.split(";")[2].split("@")[15].split(",")[0]),
    "best_supply_num4": lambda x: int(x.split(";")[2].split("@")[20].split(",")[0]),
    "best_supply_num5": lambda x: int(x.split(";")[2].split("@")[25].split(",")[0]),
}


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


def get_ticker_real_time_new(stock_id, session) -> dict:
    init_vars_dict = {}
    response = session.get(TSE_ISNT_INFO_URL.format(stock_id), timeout=10)

    if response.text.split(";")[2] != "":
        for y in res_lambda_dict.keys():
            try:
                init_vars_dict[y] = res_lambda_dict[y](response.text)
            except:
                init_vars_dict[y] = None
    else:
        for y in res_lambda_dict.keys():
            init_vars_dict[y] = stock_id

    # in some cases last price or adj price is undefined
    try:
        init_vars_dict['last_price'] = int(response.text.split()[1].split(",")[1])
    except (ValueError, IndexError):  # When instead of number value is `F`
        init_vars_dict['last_price'] = None
    try:
        init_vars_dict['adj_close'] = int(response.text.split()[1].split(",")[2])
    except (ValueError, IndexError):
        init_vars_dict['adj_close'] = None
    return init_vars_dict


def live_stock_fetcher():
    with open(ALL_INDEX_DIR, encoding="utf8", mode="r") as reader:
        loaded_json = json.loads(reader.read())
    future_to_symbol = {}
    stock_to_future = {}
    with futures.ThreadPoolExecutor(max_workers=30) as executor:
        session = requests_retry_session()
        for key in loaded_json.keys():
            future = executor.submit(get_ticker_real_time_new, loaded_json[key], session)
            stock_to_future[key] = future
            future_to_symbol[future] = key
        for future in futures.as_completed(future_to_symbol):
            stock_to_future[future_to_symbol[future]] = future.result()
        for stock in stock_to_future.keys():
            print(stock)
            print(f'{stock}: gheimate 4 omin best demand = {stock_to_future[stock].items()}')


live_stock_fetcher()

