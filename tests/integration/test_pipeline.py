import pytest
import asyncio
from fastapi.testclient import TestClient
import threading
from unittest.mock import patch
import pandas as pd

from app.main import app
from app.db_timeseries import arctic_db, LIBRARY_NAME

client = TestClient(app)

def test_full_pipeline_e2e():
    symbol = "TEST_PIPELINE_SYMBOL"

    ws_connected = threading.Event()

    def hit_endpoint():
        ws_connected.wait(timeout=2.0)

        general_df = pd.DataFrame([{"date": pd.Timestamp('2026-10-01'), "open": 300.0, "adjClose": 305.0, "volume": 20000, "high": 310.0, "low": 295.0, "count": 100, "value": 205000, "close": 304.0, "jdate": "1401-10-11"}])
        clients_df = pd.DataFrame([{"date": pd.Timestamp('2026-10-01'), "individual_buy_count": 20, "corporate_buy_count": 10}])

        with patch('app.tset_client.provider.download', return_value={symbol: general_df}):
            with patch('app.tset_client.provider.download_client_types_records', return_value={symbol: clients_df}):
                client.get(f"/api/stock-t-span/{symbol}/y/1/all")

    if LIBRARY_NAME in arctic_db.list_libraries():
        lib = arctic_db[LIBRARY_NAME]
        if lib.has_symbol(symbol):
            lib.delete(symbol)

    t = threading.Thread(target=hit_endpoint)
    t.start()

    with client.websocket_connect(f"/ws/market-data?symbol={symbol}") as websocket:
        ws_connected.set()

        data = websocket.receive_json()

        assert data["symbol"] == symbol
        assert len(data["data"]) > 0
        assert data["data"][0]["open"] == 300.0

    t.join()

    # Verify it was saved to ArcticDB
    lib = arctic_db[LIBRARY_NAME]
    assert lib.has_symbol(symbol)
    saved_df = lib.read(symbol).data
    assert not saved_df.empty
    assert saved_df.iloc[0]["open"] == 300.0
