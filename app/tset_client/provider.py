from typing import List, Optional
import pandas as pd

from app.core.provider_interface import ProviderInterface
from app.schemas.stock import StockAllSchema, StockChartSchema, StockGeneralSchema
from app.tset_client.download import download, download_client_types_records


class TSETMCProvider(ProviderInterface):
    def get_stock_current_price(self, symbol: str) -> Optional[float]:
        """Fetch the current price of a stock."""
        pass

    def get_intraday_chart(self, symbol: str) -> List[StockChartSchema]:
        """Fetch intraday chart data for a stock."""
        pass

    def get_historical_data(self, symbol: str) -> List[StockAllSchema]:
        """Fetch historical data for a stock."""
        download_general = download(symbols=[symbol], include_jdate=True)
        download_clients = download_client_types_records(symbols=[symbol], include_jdate=True)

        if symbol not in download_general:
            return []

        df_general = download_general[symbol]

        if symbol in download_clients:
            df_clients = download_clients[symbol]
            df_general['date'] = pd.to_datetime(df_general['date'])
            df_clients['date'] = pd.to_datetime(df_clients['date'])
            df_merged = pd.merge(df_general, df_clients, on='date', how='left')
        else:
            df_merged = df_general

        records = []
        for row in df_merged.itertuples():
            record_dict = row._asdict()
            clean_dict = {k: (v if pd.notna(v) else None) for k, v in record_dict.items() if k != 'Index'}

            if 'date' in clean_dict and isinstance(clean_dict['date'], pd.Timestamp):
                clean_dict['date'] = clean_dict['date'].date()

            if 'jdate' in clean_dict:
                clean_dict.pop('jdate')

            try:
                records.append(StockAllSchema(**clean_dict))
            except Exception as e:
                pass

        return records
