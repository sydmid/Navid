import os
from app import create_app
from app.main.tset_client import Downloader
import pandas as pd
import asyncio

# downloader = Downloader(mode='save_csv')
#
# asyncio.run(downloader.download())
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.run(port=5000, debug=True)
