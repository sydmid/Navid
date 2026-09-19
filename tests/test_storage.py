import pytest
import pandas as pd
from app.storage.timeseries import write_stock_data, read_stock_data

def test_timeseries_storage():
    # Setup mock data
    symbol = "TEST_STORAGE_SYMBOL"
    df = pd.DataFrame([
        {
            "date": pd.Timestamp('2023-01-01'),
            "open": 100.0,
            "close": 105.0
        }
    ])

    # Write to ArcticDB
    write_stock_data(symbol, df)

    # Read back from ArcticDB
    read_df = read_stock_data(symbol)

    # Verify
    assert read_df is not None
    assert not read_df.empty
    assert read_df.iloc[0]['open'] == 100.0
    assert read_df.iloc[0]['close'] == 105.0

def test_timeseries_storage_not_found():
    symbol = "NOT_FOUND_SYMBOL"
    read_df = read_stock_data(symbol)
    assert read_df is None
