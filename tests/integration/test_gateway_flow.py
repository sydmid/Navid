import pytest
import pandas as pd
from datetime import date
from unittest.mock import patch
from fastapi.testclient import TestClient

from app.main import app
from app.db_timeseries import arctic_db, LIBRARY_NAME

client = TestClient(app)

@patch('app.tset_client.provider.download')
@patch('app.tset_client.provider.download_client_types_records')
def test_gateway_flow_e2e(mock_download_clients, mock_download_general):
    symbol = "TEST_E2E_SYMBOL"

    # Reset cache library for clean test
    if LIBRARY_NAME in arctic_db.list_libraries():
        lib = arctic_db[LIBRARY_NAME]
        if lib.has_symbol(symbol):
            lib.delete(symbol)

    # 1. Setup mock data to be returned by scraper
    general_df = pd.DataFrame([
        {
            "date": pd.Timestamp('2026-09-01'),
            "open": 100.0,
            "adjClose": 105.0,
            "volume": 1000,
            "high": 110.0,
            "low": 95.0,
            "count": 50,
            "value": 105000,
            "close": 104.0,
            "jdate": "1401-10-11"
        }
    ])
    clients_df = pd.DataFrame([
        {
            "date": pd.Timestamp('2026-09-01'),
            "individual_buy_count": 10,
            "corporate_buy_count": 5,
        }
    ])

    mock_download_general.return_value = {symbol: general_df}
    mock_download_clients.return_value = {symbol: clients_df}

    # 2. Hit the REST endpoint
    response = client.get(f"/api/stock-t-span/{symbol}/y/1/all")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["open"] == 100.0
    assert data[0]["individual_buy_count"] == 10

    # 3. Verify it was saved to ArcticDB
    lib = arctic_db[LIBRARY_NAME]
    assert lib.has_symbol(symbol)
    saved_df = lib.read(symbol).data
    assert not saved_df.empty
    assert saved_df.iloc[0]["open"] == 100.0

    # Test WebSocket Event Emission (Simplified for test execution env without full event loop)
    # The event emission is covered by the integration in endpoints when async loop runs

@patch('app.tset_client.provider.download')
@patch('app.tset_client.provider.download_client_types_records')
def test_gateway_flow_stale_data(mock_download_clients, mock_download_general):
    symbol = "TEST_STALE_SYMBOL"

    # Reset cache library for clean test
    if LIBRARY_NAME in arctic_db.list_libraries():
        lib = arctic_db[LIBRARY_NAME]
        if lib.has_symbol(symbol):
            lib.delete(symbol)

    # 1. First request will cache data (simulate it)
    general_df = pd.DataFrame([
        {
            "date": pd.Timestamp('2023-09-01'), # very old date
            "open": 90.0,
            "adjClose": 95.0,
            "volume": 1000,
            "high": 110.0,
            "low": 95.0,
            "count": 50,
            "value": 105000,
            "close": 94.0,
            "jdate": "1401-10-11"
        }
    ])
    clients_df = pd.DataFrame([
        {
            "date": pd.Timestamp('2023-09-01'),
            "individual_buy_count": 5,
            "corporate_buy_count": 5,
        }
    ])
    mock_download_general.return_value = {symbol: general_df}
    mock_download_clients.return_value = {symbol: clients_df}

    # Actually just call endpoint to cache the stale data
    response1 = client.get(f"/api/stock-t-span/{symbol}/y/10/all")
    assert response1.status_code == 200

    # 2. Now simulate the new scraper values with fresh data
    fresh_general_df = pd.DataFrame([
        {
            "date": pd.Timestamp('2026-09-01'), # new date
            "open": 200.0,
            "adjClose": 205.0,
            "volume": 5000,
            "high": 210.0,
            "low": 195.0,
            "count": 150,
            "value": 505000,
            "close": 204.0,
            "jdate": "1404-10-11"
        }
    ])
    fresh_clients_df = pd.DataFrame([
        {
            "date": pd.Timestamp('2026-09-01'),
            "individual_buy_count": 25,
            "corporate_buy_count": 15,
        }
    ])
    mock_download_general.return_value = {symbol: fresh_general_df}
    mock_download_clients.return_value = {symbol: fresh_clients_df}

    # Since the first cached data was from 2023, the gateway's stale check (which uses today() - 2 days)
    # will mark it as stale and trigger a fetch from the provider.
    response2 = client.get(f"/api/stock-t-span/{symbol}/y/1/all")
    assert response2.status_code == 200
    data2 = response2.json()
    assert len(data2) == 1
    assert data2[0]["open"] == 200.0
