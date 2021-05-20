import requests as req
import re
import json
from bs4 import BeautifulSoup as soup
import pandas as pd
from datetime import datetime
import os

# Directories
ALL_INDEX_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'../data/index_all.json'))

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

class TSE(object):
    def __init__(self):
        self.index_list = []
    # @classmethod
    # def current_indexer(cls):
    #     with open()

    def get_index_list(self):
        if len(self.index_list) > 1:
            return self.index_list
        self.styled_printer("Sending Request...","i")
        res = req.post(INDEX_LIST, data={"id":""})
        res_json = json.loads(res.text)
        for json_item in res_json:
            self.index_list.append([json_item["LVal18AFC"], json_item["InstrumentID"]])
        return self.index_list

    def get_inscode(self, symbol):
        res = req.get(INDEX_INFO + symbol)
        pattern = re.compile(r"'inscode': '\d+'")
        match = re.search(pattern, res.text)
        inscode = re.search(r"\d+", match.group())
        return inscode.group()

    @classmethod
    def get_index_all_tablo(cls):
        # with open(ALL_INDEX_DIR, encoding="utf8") as reader:
            # json_indexes = json.loads(reader.read())
        res = req.get(INDEX_ALL_TABLO)
        doc = soup(res.text, 'html.parser')
        # with open(os.path.join(os.path.dirname(__file__), 'index.html'), mode='w', encoding="utf8") as f:
        #     f.write(res.text)
        for x in doc.find_all("tr"):
            print(x.contents)

    def get_index_info(self, symbol, inscode=None):
        if inscode is None:
            inscode = self.get_inscode(symbol)
        print(INDEX_DATA + inscode)
        res = req.get(INDEX_DATA + inscode)
        doc = soup(res.text, 'html.parser')
        latest_trans = doc.table.find_all("tr")[1].find_all("td")[1].string
        latest_price = doc.table.find_all("tr")[2].find_all("td")[1]
        latest_price_value = latest_price.find_all("span")[0].string
        latest_price_change = latest_price.find_all("span")[1].string
        if '(' in latest_price_change:
            latest_price_change = "-" + latest_price_change.replace('(','').replace(')','').replace(' ','')

        close_price = doc.table.find_all("tr")[3].find_all("td")[1]
        CLOSE = close_price.find_all("span")[0].string
        close_price_change = close_price.find_all("span")[1].string
        if '(' in close_price_change:
            close_price_change = "-" + close_price_change.replace('(','').replace(')','').replace(' ','')

        VOL = doc.table.find_all("tr")[5].find_all("td")[1].string
        price_lower_bound = doc.table.find_all("tr")[7].find_all("td")[1].string.split("-")[0]
        price_upper_bound = doc.table.find_all("tr")[7].find_all("td")[1].string.split("-")[1]

        OPEN = doc.table.find_all("tr")[3].find_all("td")[3].string
        LOW = doc.table.find_all("tr")[1].find(id="PriceMin").string
        HIGH = doc.table.find_all("tr")[1].find(id="PriceMax").string

        # convert strings to integer
        OPEN = int(OPEN.replace(',',''))
        LOW = int(LOW.replace(',',''))
        HIGH = int(HIGH.replace(',',''))
        CLOSE = int(CLOSE.replace(',',''))
        VOL = int(VOL.replace(',',''))
        latest_price_value = int(latest_price_value.replace(',',''))
        latest_price_change = float(latest_price_change)
        price_lower_bound = int(price_lower_bound.replace(',',''))
        price_upper_bound = int(price_upper_bound.replace(',',''))

        res_dict = {"OPEN":OPEN, "LOW":LOW, "HIGH": HIGH, "CLOSE":CLOSE, "VOLUME": VOL,
                   "LAST_PRICE":latest_price_value, "LAST_PRICE_CHANGE":latest_price_change,
                  "PRICE_LOW_BOUND": price_lower_bound, "PRICE_UP_BOUND":price_upper_bound}
        return res_dict

    def get_latest_msgs(self):
        res = req.get(NAZER_MSGS)
        res_json = json.loads(res.text)
        msgs = res_json['nazerMsg']
        messages = []
        for msg in msgs:
            tmp = {"time": msg['w'],
                  "title": msg['t'],
                  "content": msg['c']}
            messages.append(tmp)
        return messages

    def get_index_msgs(self, symbol, index_id=None):
        if index_id == None:
            self.get_index_list()
            for index in self.index_list:
                if index[0]==symbol:
                    index_id = index[1]
                    break
        if index_id==None:
            self.styled_printer("ERROR. Could not retrieve InstrumentID of " + symbol,"e")
            return None
        res = req.get(NAZER_MSGS_INDEX.format(index_id))
        try:
            res_json = json.loads(res.text)
        except json.JSONDecodeError as json_err:
            self.styled_printer("Error in Parsing Json response.","e")
            return None
        messages = []
        for msg in res_json["data"]:
            tmp = {"time": msg[0],
                   "title": msg[1],
                   "content": msg[2]}
            messages.append(tmp)
        return messages


    def get_overall_info(self):
        res = req.get(OVERALL_INFO)
        res_soup = soup(res.text)
        tbl = res_soup.find_all("table")[0]
        market_status = "OPEN" if "باز" in tbl.find_all("tr")[0].find_all("td")[1] else "CLOSE"
        overall_index = tbl.find_all("tr")[1].find_all("td")[1].get_text().split(' ')[0]
        if "mn" in tbl.find_all("tr")[1].find_all("td")[1].div.get("class")[0]:
            overall_index_change = "-" + tbl.find_all("tr")[1].find_all("td")[1].get_text().split(' ')[1]
        else:
            overall_index_change = tbl.find_all("tr")[1].find_all("td")[1].get_text().split(' ')[1]
        overall_equivalent_index = tbl.find_all("tr")[2].find_all("td")[1].get_text().split(' ')[0]
        if "mn" in tbl.find_all("tr")[2].find_all("td")[1].div.get("class")[0]:
            overall_equivalent_index_change = "-" + tbl.find_all("tr")[2].find_all("td")[1].get_text().split(' ')[1]
        else:
            overall_equivalent_index_change = tbl.find_all("tr")[2].find_all("td")[1].get_text().split(' ')[1]
        overall_volume = tbl.find_all("tr")[7].find_all("td")[1].div.get("title")

        # convert string to number
        overall_index = float(overall_index.replace(',',''))
        overall_index_change = float(overall_index_change.replace(',',''))
        overall_equivalent_index = float(overall_equivalent_index.replace(',',''))
        overall_equivalent_index_change = float(overall_equivalent_index_change.replace(',',''))
        overall_volume = int(overall_volume.replace(',',''))

        res_dict = {"MARKET_STATUS": market_status,
                    "OVERALL_INDEX": overall_index,
                    "OVERALL_INDEX_CHANGE": overall_index_change,
                    "EQUIVALENT_INDEX": overall_equivalent_index,
                    "EQUIVALENT_INDEX_CHANGE": overall_equivalent_index,
                    "OVERALL_VOLUME": overall_volume}
        return res_dict

    def get_index_all_history(self, symbol, inscode=None):
        if inscode==None:
            inscode = self.get_inscode(symbol)

        res = req.get(INDEX_ALL_HISTORY+inscode)
        res_json = json.loads(res.text)
        df = pd.DataFrame(res_json, columns=["Date","Open","High","Low","Close","Volume"])
        for i in range(df.shape[0]):
            df.iloc[i,0] = df.iloc[i,0]/1000
        df.Date = df.Date.apply(lambda x: datetime.fromtimestamp(x).date())
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.set_index("Date")
        return df

    def get_index_history(self, symbol, startDate, endDate, index_id=None):
        if index_id==None or index_id=="":
            if len(self.index_list)<1:
                self.get_index_list()
            for item in self.index_list:
                if symbol==item[0]:
                    index_id=item[1]
                    break

        payload = {"symboldatapara": symbol,
          "inscodesymbol": index_id,
          "symbolStart": startDate,
          "symbolEnd": endDate}
        res = req.post(INDEX_HISTORY, params=payload)
        res_soup = soup(res.text)
        table = res_soup.table
        rows = table.find_all("tr")[1:]
        data = []
        for row in rows:
            tdate = row.find_all("td")[1].string
            topen = float(row.find_all("td")[10].string)
            tclose = float(row.find_all("td")[6].string)
            thigh = float(row.find_all("td")[9].string)
            tlow = float(row.find_all("td")[8].string)
            tvol = float(row.find_all("td")[4].string)
            data.append([tdate,int(topen),int(tlow),int(thigh),int(tclose),int(tvol)])

        df = pd.DataFrame(data, columns=["Date","Open","Low","High","Close","Volume"])
        return df

    def styled_printer(self,msg,msg_type='error',end='\n\r'):
        # template: \x1b[ style;foreground_color;background_color m\x1b[0m
        # style in range(0,8), fg in range(30,38), bg in range(40,48)
        switcher = {
            'w':       "\x1b[1;37;43m{}\x1b[0m",
            'warning': "\x1b[1;37;43m{}\x1b[0m",
            'e':       "\x1b[0;37;41m{}\x1b[0m",
            'error':   "\x1b[0;37;41m{}\x1b[0m",
            'i':       "\x1b[0;37;44m{}\x1b[0m",
            'info':    "\x1b[0;37;44m{}\x1b[0m"}
        template = switcher.get(msg_type,'_{}_')
        print(template.format(msg),end=end)

    def candle_chart(self, dataframe_olhcv, startDate=None, endDate=None):
        try:
            import mplfinance as mplf
        except ImportError as er:
            self.styled_printer("mplfinance package is needed to plot candle chart. \nRun [pip install mplfinance] to install mplfinance.","e")

        if startDate != None:
            dataframe_olhcv = dataframe_olhcv[ dataframe_olhcv.index >= startDate]
        if endDate != None:
            dataframe_olhcv = dataframe_olhcv[ dataframe_olhcv.index <= endDate]
        mplf.plot(dataframe_olhcv, type='candle', volume=True, show_nontrading=False,style='yahoo')

