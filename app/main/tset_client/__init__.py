import os
import datetime

from .download import download
from .download import download_client_types_records
from .symbols_data import all_symbols
from .ticker import Ticker
from .config import TRY_COUNT

_tset_client_dir = os.path.abspath(os.path.dirname(__file__))
_downloaded_date_path = os.path.normpath(os.path.join(_tset_client_dir, 'download/Dates.txt'))
_logs_path = os.path.normpath(os.path.join(_tset_client_dir, 'download/Logs.txt'))

Download_path_1 = os.path.normpath(os.path.join(_tset_client_dir, 'download/general_records'))
Download_path_2 = os.path.normpath(os.path.join(_tset_client_dir, 'download/client_records'))
Download_path_test = os.path.normpath(os.path.join(_tset_client_dir, 'download/test'))


class Downloader:
    biggest_date = datetime.date.min

    def __init__(self):
        self.tries = 0

    def test(self):
        self.tries += 1
        print(self.tries)

    def update(self, mode="test_download"):
        if mode == "csv_download":
            if self.tries < TRY_COUNT:
                self.tries += 1
                self._csv_download()
            else:
                self.tries = 0
                return "can't do it, the maximum tries has exceeded it's limit"
        else:
            return self._test_download()

    def _csv_download(self):
        print(f"update process has started, Number of tries so far:{self.tries}")
        if os.path.exists(_downloaded_date_path):
            try:
                stocks_to_lookup = download(
                    ["فولاد", "آپ", "بورس", "البرز", "حکشتی", "ونیکی", "فرابورس", "تاپیکو", "وبملت",
                     "بجهرم"], include_jdate=True)
                for stock, content in stocks_to_lookup.items():
                    dates = content[list(content.keys())[0]].keys()
                    if dates[len(dates) - 1] > self.biggest_date:
                        self.biggest_date = dates[len(dates) - 1]
                print(f"The Biggest is : {self.biggest_date}")
                try:
                    with open(_downloaded_date_path, "r") as f:
                        current_date_value = f.readline()
                        date_time_obj = datetime.datetime.strptime(current_date_value, '%Y-%m-%d %H:%M:%S')
                        print(f"current date value is: {current_date_value}")

                    if not current_date_value or date_time_obj < self.biggest_date:
                        print("Starting to Download All")
                        download(symbols="all", write_to_csv=True, base_path=Download_path_test)
                    else:
                        print("Data is Up to Date. There's Nothing More to Do :)")
                        with open(_logs_path, "a") as logfile:
                            logfile.write(f"Data is Up to Date Attempt {datetime.date.today()}\n")
                        return
                except:
                    self.update()
                with open(_downloaded_date_path, "w+") as f:
                    f.write(str(self.biggest_date))

                with open(_logs_path, "a") as f:
                    f.write(f"Successful Attempt {datetime.date.today()}\n")

            except:
                print("Couldn't Lookup retrying...")
                self.update()
        else:
            f = open(_downloaded_date_path, "w+")
            f.close()
            print("There was no Date.txt. Now There is one ;)")
            self.update()

    def _test_download(self):
        print(f"test process has started number of tries so far:{self.tries}")
        try:
            return download(symbols=["فولاد", "آپ", "بورس"], base_path=Download_path_test)
        except:
            print("Couldn't Lookup retrying...")

