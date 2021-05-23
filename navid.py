import os

from app import create_app

app = create_app(os.getenv('CONFIG_NAME') or 'default')
app.run(port=5000, debug=True)
