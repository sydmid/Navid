import os
# import asyncio

from app import create_app
# from app.create_tables import create_tset_tables

# asyncio.run(create_tset_tables())

app = create_app(os.getenv('CONFIG_NAME') or 'default')
app.run(port=5000, debug=True)
