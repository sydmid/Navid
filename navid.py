import os
from app import create_app
from app.main.tset_client import CsvUpdater

csv_updater = CsvUpdater()
csv_updater.update()

# app.run(port=5000, debug=True)
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
