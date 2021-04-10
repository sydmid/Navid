import os
import pandas as pd
import asyncio

from app import create_app
from app.main.init_db import init_db
from app.main.tset_client import Downloader

# Initialize for the First Time Deploying the app
# asyncio.run(init_db())

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.run(port=5000, debug=True)

