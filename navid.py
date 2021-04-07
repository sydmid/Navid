import os
from app import create_app
from app.main.tset_client import Downloader
from app.main.models.record import Record
import pandas as pd



# downloader.update(mode="csv_download")
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.run(port=5000, debug=True)
