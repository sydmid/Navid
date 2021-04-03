import os
from app.main import create_app
from app.main.tset_client import csv_updater

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    # csv_updater()
    app.run(port=5000, debug=True)
