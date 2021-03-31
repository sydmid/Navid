import os
import datetime

from .download import download
from .download import download_client_types_records
from .symbols_data import all_symbols
from .ticker import Ticker


basedir = os.path.abspath(os.path.dirname(__file__))
Dates_path = os.path.normpath(os.path.join(basedir, 'download/Dates.txt'))
Logs_path = os.path.normpath(os.path.join(basedir, 'download/Logs.txt'))

Download_path_1 = os.path.normpath(os.path.join(basedir, 'download/general_records'))
Download_path_2 = os.path.normpath(os.path.join(basedir, 'download/client_records'))
Download_path_test = os.path.normpath(os.path.join(basedir, 'download/test'))


def controlled_download():
    print("Starting Controlled Download")
    biggest_date = datetime.date.min
    if os.path.exists(Dates_path):
        try:
            stocks_to_lookup = download(["فولاد", "آپ", "بورس", "البرز", "حکشتی", "ونیکی", "فرابورس", "تاپیکو", "وبملت",
                                        "بجهرم"], include_jdate=True)
            for stock, content in stocks_to_lookup.items():
                dates = content[list(content.keys())[0]].keys()
                if dates[len(dates) - 1] > biggest_date:
                    biggest_date = dates[len(dates) - 1]
            print(f"The Biggest is : {biggest_date}")
            try:
                with open(Dates_path, "r") as f:
                    current_date_value = f.readline()
                    date_time_obj = datetime.datetime.strptime(current_date_value, '%Y-%m-%d %H:%M:%S')
                    print(f"current date value is: {current_date_value}")
                    #
                    if not current_date_value or date_time_obj < biggest_date:
                        print("Starting to Download All")
                        download(symbols="all", write_to_csv=True, base_path=Download_path_test)
                    else:
                        print("Data is Up to Date. There's Nothing More to Do :)")
                        with open(Logs_path, "a") as f:
                            f.write(f"Data is Up to Date Attempt {datetime.date.today()}\n")
                        return
            except:
                controlled_download()
            with open(Dates_path, "w+") as f:
                f.write(str(biggest_date))
            # Implementing Some Log Mechanism
            with open(Logs_path, "a") as f:
                f.write(f"Successful Attempt {datetime.date.today()}")

        except:
            print("Couldnt Lookup retrying...")
            # Add some Timer or Rule
            controlled_download()
    else:
        f = open(Dates_path, "w+")
        f.close()
        print("There was no Date.txt. Now There is one ;)")
        controlled_download()

