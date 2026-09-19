from typing import Optional
import pandas as pd
from app.db_timeseries import market_data_lib

def write_stock_data(symbol: str, df: pd.DataFrame) -> None:
    """Write stock DataFrame to ArcticDB."""
    if df.empty:
        return
    # Store df using the symbol as the symbol in Arctic
    market_data_lib.write(symbol, df)

def read_stock_data(symbol: str) -> Optional[pd.DataFrame]:
    """Read stock DataFrame from ArcticDB."""
    if market_data_lib.has_symbol(symbol):
        item = market_data_lib.read(symbol)
        return item.data
    return None
