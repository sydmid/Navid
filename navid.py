import os
from app import create_app
from app.main.tset_client import csv_updater

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# csv_updater()
app.run(port=5000, debug=True)
