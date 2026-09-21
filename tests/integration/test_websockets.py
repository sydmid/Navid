import pytest
import asyncio
from fastapi.testclient import TestClient
import threading
from unittest.mock import patch
import pandas as pd

from app.main import app
from app.db_timeseries import arctic_db, LIBRARY_NAME

client = TestClient(app)

def test_websocket_event_driven_flow():
    symbol = "TEST_WS_SYMBOL"

    # We will use threading to simulate concurrent API access, but we'll use a threading.Event
    # to coordinate the sync execution and avoid sleep()
    ws_connected = threading.Event()

    def hit_endpoint():
        # Wait for websocket to connect cleanly
        ws_connected.wait(timeout=2.0)

        general_df = pd.DataFrame([{"date": pd.Timestamp('2026-09-01'), "open": 150.0, "adjClose": 155.0, "volume": 10000, "high": 110.0, "low": 95.0, "count": 50, "value": 105000, "close": 155.0, "jdate": "1401-10-11"}])
        clients_df = pd.DataFrame([{"date": pd.Timestamp('2026-09-01'), "individual_buy_count": 10, "corporate_buy_count": 5}])

        with patch('app.tset_client.provider.download', return_value={symbol: general_df}):
            with patch('app.tset_client.provider.download_client_types_records', return_value={symbol: clients_df}):
                # This request causes GatewayProvider to fetch data (if cache is missing) and publish to event_bus
                client.get(f"/api/stock-t-span/{symbol}/y/1/all")

    if LIBRARY_NAME in arctic_db.list_libraries():
        lib = arctic_db[LIBRARY_NAME]
        if lib.has_symbol(symbol):
            lib.delete(symbol)

    t = threading.Thread(target=hit_endpoint)
    t.start()

    with client.websocket_connect(f"/ws/market-data?symbol={symbol}") as websocket:
        ws_connected.set()

        # Block until the endpoint thread publishes the message and websocket pushes it
        data = websocket.receive_json()

        assert data["symbol"] == symbol
        assert len(data["data"]) > 0
        assert data["data"][0]["open"] == 150.0

    t.join()
