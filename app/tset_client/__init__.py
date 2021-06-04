import os
import datetime

from .download import download
from .download import download_client_types_records

from .symbols_data import all_symbols
from .ticker import Ticker

_tset_client_dir = os.path.abspath(os.path.dirname(__file__))
_downloaded_date_path = os.path.normpath(os.path.join(_tset_client_dir, 'download/Dates.txt'))
_logs_path = os.path.normpath(os.path.join(_tset_client_dir, 'download/Logs.txt'))

Download_path_1 = os.path.normpath(os.path.join(_tset_client_dir, 'download/general_records'))
Download_path_2 = os.path.normpath(os.path.join(_tset_client_dir, 'download/client_records'))
Download_path_test = os.path.normpath(os.path.join(_tset_client_dir, 'download/test'))


class Downloader:
    try_count = 0
    options = {
        "max_tries": None,
        "mode": None
    }

    def __init__(self, max_tries=10, mode='test'):
        self.options['max_tries'] = max_tries
        self.options['mode'] = mode

    async def download(self):
        print('download has started')
        downloaded = dict()
        if self.options['mode'] == 'save_csv':
            print('mode = save_csv')
            try:
                downloaded = await self._csv_downloader(await self._latest_date_fetcher())
            except Exception as err:
                print('some thing went wrong with downloading from tsetmc', str(err))
                await self._retry_handler()
        elif self.options['mode'] == 'production':
            print('mode = production')
            try:
                downloaded = download(symbols="all", include_jdate=True)
            except Exception as err:
                print('some thing went wrong with downloading from tsetmc', str(err))
                await self._retry_handler()
        elif self.options['mode'] == 'test':
            print('mode = test')
            try:
                downloaded = download(symbols=["خودرو", "فولاد"], include_jdate=True)
            except Exception as err:
                print('some thing went wrong with downloading from tsetmc', str(err))
                await self._retry_handler()

        return downloaded

    async def _retry_handler(self):
        self.try_count += 1
        print(f"number of retries: {self.try_count} so far")
        if not self.try_count < self.options['max_tries']:
            return False
        await self.download()

    # Only First Group of data
    async def _csv_downloader(self, biggest_date):
        downloaded = ''
        if not os.path.exists(_downloaded_date_path):
            new_date_file = open(_downloaded_date_path, "w+")
            new_date_file.close()
        with open(_downloaded_date_path, "r") as f:
            current_saved_date_value = f.readline()
            date_time_obj = datetime.datetime.strptime(current_saved_date_value, '%Y-%m-%d %H:%M:%S')
            print(f"current date value is: {current_saved_date_value}")

        if not current_saved_date_value or date_time_obj < biggest_date:
            print("Starting to Download All")
            downloaded = download(symbols="all", write_to_csv=True, base_path=Download_path_1)
        else:
            print("Data is Up to Date. There's Nothing More to Do :)")
            with open(_logs_path, "a") as logfile:
                logfile.write(f"Data is Up to Date Attempt {datetime.date.today()}\n")
        return downloaded

    async def _latest_date_fetcher(self):
        biggest_data = datetime.date.min
        stocks_to_lookup = download(
            ["فولاد", "آپ", "بورس", "البرز", "حکشتی", "ونیکی", "فرابورس", "تاپیکو", "وبملت",
             "بجهرم"], include_jdate=True)
        for stock, content in stocks_to_lookup.items():
            dates = content[list(content.keys())[0]].keys()
            if dates[len(dates) - 1] > biggest_data:
                biggest_data = dates[len(dates) - 1]
        return biggest_data

    def initialize_existing_db(self):
        downloaded = dict()
        try:
            downloaded['download-general'] = download(symbols='all', include_jdate=True)
            downloaded['download-clients'] = download_client_types_records(symbols='all', include_jdate=True)
            return downloaded
        except Exception as err:
            print('some thing went wrong with downloading from tsetmc', str(err))

    def update_existing_db(self):
        downloaded = dict()
        try:
            downloaded['download-general'] = download(symbols='all', include_jdate=True)
            downloaded['download-clients'] = download_client_types_records(symbols='all', include_jdate=True)
            return downloaded
        except Exception as err:
            print('some thing went wrong with downloading from tsetmc', str(err))
