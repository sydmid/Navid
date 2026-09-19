from arcticdb import Arctic
from app.core.config import settings

# Initialize Arctic DB connection
arctic_db = Arctic(settings.ARCTICDB_URI)

# Ensure the library for market data exists
LIBRARY_NAME = "market_data"

if LIBRARY_NAME not in arctic_db.list_libraries():
    arctic_db.create_library(LIBRARY_NAME)

market_data_lib = arctic_db[LIBRARY_NAME]
