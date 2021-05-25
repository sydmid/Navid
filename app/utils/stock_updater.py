import os
import time
import re
import json
import requests as req
from bs4 import BeautifulSoup as soup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException

# Directories
ALL_INDEX_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/index_all.json'))
ALL_NO_INDEX_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/index_no_all.json'))
ALL_YES_INDEX_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/index_yes_all.json'))
MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../models/stock'))
TSET_CLIENT_ALL_SYMBOLS = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tset_client/data/symbols_name.json'))
base_dir = os.path.abspath(os.path.dirname(__file__))

# URLs
OVERALL_INFO = "http://www.tsetmc.com/Loader.aspx?ParTree=15"
NAZER_MSGS = "http://tse.ir/json/HomePage/nazerMSG.json"
NAZER_MSGS_INDEX = "http://tse.ir/json/Instrument/NazerMessages/NazerMessages_{}.json"
INDEX_LIST = "http://www.fipiran.com/DataService/AutoCompletesymbol"
INDEX_INFO = "http://www.fipiran.com/Symbol?symbolpara="
INDEX_DATA = "http://www.fipiran.com/Symbol/_priceData?inscode="
INDEX_HISTORY = "http://www.fipiran.com/DataService/Exportsymbol"
INDEX_ALL_HISTORY = "http://www.fipiran.com/Symbol/MarketQoutes?inscode="
INDEX_ALL_TABLO = "http://tablokhani.com/NewDash"


def get_inscode(symbol):
    res = req.get(INDEX_INFO + symbol)
    pattern = re.compile(r"'inscode': '\d+'")
    match = re.search(pattern, res.text)
    inscode = re.search(r"\d+", match.group())
    return inscode.group()


async def add_new_stocks():
    print("adding namad+inscode to json bank started")
    dict_to_add = dict()
    final_dict = dict()
    with open(ALL_NO_INDEX_DIR, encoding="utf8", mode="r") as reader:
        json_nos = json.loads(reader.read())
        for x in range(len(json_nos)):
            dict_to_add[json_nos[x]] = get_inscode(json_nos[x])
    with open(ALL_INDEX_DIR, encoding="utf8", mode="r") as reader:
        json_indexes = json.loads(reader.read())
    with open(ALL_INDEX_DIR, encoding="utf8", mode="w") as writer:
        final_dict = {**dict_to_add, **json_indexes}
        writer.write(json.dumps(final_dict, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': ')))
    with open(TSET_CLIENT_ALL_SYMBOLS, encoding="utf8", mode="r") as reader:
        current_symbols_json = json.loads(reader.read())
        if current_symbols_json == final_dict:
            return
    backup_file_name = time.strftime('%A%Y%m%H%M%S')
    os.rename(TSET_CLIENT_ALL_SYMBOLS, os.path.join(base_dir, f'../tset_client/data/{backup_file_name}.json'))
    with open(TSET_CLIENT_ALL_SYMBOLS, encoding="utf8", mode="w") as writer:
        final_dict = {**dict_to_add, **json_indexes}
        writer.write(json.dumps(final_dict, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': ')))


def to_farsi(string: str):
    return string.replace('ك', 'ک').replace('ي', 'ی').strip()


async def update_json_bank():
    print("updating json bank started")

    def _fresh_element_getter(driver):
        count = 0
        while count < 20:
            count += 1
            if count > 20:
                print("time out for 10 seconds")
                return
            time.sleep(.5)
            try:
                elem = driver.find_element_by_id('main_bazar_body')
                return driver.page_source
            except StaleElementReferenceException:
                continue
    opts = Options()
    opts.headless = True
    assert opts.headless
    chrome_driver = Chrome(options=opts, executable_path=os.path.join(os.path.dirname(__file__), 'chromedriver.exe'))
    chrome_driver.get('http://tablokhani.com/NewDash')
    index_name_list = []
    doc = soup(_fresh_element_getter(chrome_driver), 'html.parser')
    for x in doc.find(id="main_bazar_body").contents:
        index_name_list.append(x.a.text)
    chrome_driver.close()
    with open(ALL_INDEX_DIR, encoding="utf8") as reader:
        json_indexes = json.loads(reader.read())
        oks = []
        nos = []
        for namad in index_name_list:
            try:
                json_indexes[namad]
                # print(f"namad {namad} is ok with inscode {json_indexes[str(namad)]}")
                oks.append(namad)
            except:
                nos.append(namad)

        with open(ALL_NO_INDEX_DIR, mode='w', encoding="utf8") as writer:
            writer.write(json.dumps(nos, ensure_ascii=False))

        with open(ALL_YES_INDEX_DIR, mode='w', encoding="utf8") as writer:
            writer.write(json.dumps(oks, ensure_ascii=False))


async def write_model_file():
    with open(ALL_NO_INDEX_DIR, mode='r', encoding='utf8') as reader:
        json_list = json.loads(reader.read())
        if len(json_list) == 0:
            print(f'something went wrong this is your index_no_all.json:\n\
                  {reader.read()}')
            raise
    model_file_name = time.strftime('%A%Y%m%H%M%S')
    print("writing to model files started")
    new_list = []
    with open(ALL_NO_INDEX_DIR, encoding="utf8", mode="r+") as reader:
        json_data = json.loads(reader.read())
        for x in range(len(json_data)):
            new_list.append(to_farsi(json_data[x]))
    with open(os.path.join(MODELS_DIR, f"{model_file_name}.py"), mode='w', encoding='utf8') as f:
        f.write("from app.db import db \n")
        for x in range(len(new_list)):
            f.write(f"class {new_list[x]}(db.Model):\n\
    __tablename__ = '{new_list[x]}'\n\
\n\
    name = db.Column(db.String(15))\n\
    group = db.Column(db.String(30))\n\
    date = db.Column(db.Date, primary_key=True)\n\
    open = db.Column(db.Float)\n\
    high = db.Column(db.Float)\n\
    low = db.Column(db.Float)\n\
    adjClose = db.Column(db.Float)\n\
    value = db.Column(db.Integer)\n\
    volume = db.Column(db.Integer)\n\
    count = db.Column(db.Integer)\n\
    close = db.Column(db.Float)\n\
    individual_buy_count = db.Column(db.Integer)\n\
    individual_sell_count = db.Column(db.Integer)\n\
    individual_buy_vol = db.Column(db.Integer)\n\
    individual_sell_vol = db.Column(db.Integer)\n\
    individual_buy_value = db.Column(db.Integer)\n\
    individual_sell_value = db.Column(db.Integer)\n\
    corporate_buy_count = db.Column(db.Integer)\n\
    corporate_sell_count = db.Column(db.Integer)\n\
    corporate_buy_vol = db.Column(db.Integer)\n\
    corporate_sell_vol = db.Column(db.Integer)\n\
    corporate_buy_value = db.Column(db.Integer)\n\
    corporate_sell_value = db.Column(db.Integer)\n\
    individual_buy_mean_price = db.Column(db.Float)\n\
    individual_sell_mean_price = db.Column(db.Float)\n\
    corporate_buy_mean_price = db.Column(db.Float)\n\
    corporate_sell_mean_price = db.Column(db.Float)\n\
    individual_ownership_change = db.Column(db.Integer)\n\
    jdate = db.Column(db.String)\n\
\n\
")


async def _exception_handling(backupfile):
    if os.path.exists(ALL_NO_INDEX_DIR):
        os.remove(ALL_NO_INDEX_DIR)
    else:
        print("The file index_no_all.json does not exist")
    if os.path.exists(ALL_YES_INDEX_DIR):
        os.remove(ALL_YES_INDEX_DIR)
    else:
        print("The file index_yes_all.json does not exist")
    with open(ALL_INDEX_DIR, mode='w', encoding='utf8') as writer:
        writer.write(json.dumps(backupfile, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': ')))


async def json_catalog_update():
    with open(ALL_INDEX_DIR, mode='r', encoding='utf8') as reader:
        json_backup = json.loads(reader.read())
    try:
        await update_json_bank()
    except:
        print('updating json bank failed')
        await _exception_handling(json_backup)
        return
    try:
        await add_new_stocks()
    except:
        print('adding name+inscode to json bank failed')
        await _exception_handling(json_backup)
        return
    try:
        await write_model_file()
    except:
        print('adding new models failed')
        await _exception_handling(json_backup)
        return

