import os
from app import create_app
from app.main.tset_client import Downloader
import pandas as pd

downloader = Downloader()

downloaded = downloader.update()
for stock in downloaded.values():
    df = pd.DataFrame(stock)
    print(df.columns)

downloader.update(mode="csv_download")
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.run(port=5000, debug=True)
