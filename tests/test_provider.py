import pytest
import pandas as pd
from datetime import date
from unittest.mock import patch, MagicMock

from app.tset_client.provider import TSETMCProvider
from app.schemas.stock import StockAllSchema

@patch('app.tset_client.provider.download')
@patch('app.tset_client.provider.download_client_types_records')
def test_tsetmc_provider_get_historical_data(mock_download_clients, mock_download_general):
    provider = TSETMCProvider()

    general_df = pd.DataFrame([
        {
            "date": pd.Timestamp('2023-01-01'),
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
            "date": pd.Timestamp('2023-01-01'),
            "individual_buy_count": 10,
            "corporate_buy_count": 5,
        }
    ])

    mock_download_general.return_value = {"TEST_SYMBOL": general_df}
    mock_download_clients.return_value = {"TEST_SYMBOL": clients_df}

    records = provider.get_historical_data("TEST_SYMBOL")

    assert len(records) == 1
    assert isinstance(records[0], StockAllSchema)
    assert records[0].date == date(2023, 1, 1)
    assert records[0].open == 100.0
    assert records[0].individual_buy_count == 10
