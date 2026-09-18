from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import date
import pandas as pd

from app.schemas.stock import StockAllSchema, StockChartSchema, StockGeneralSchema

class ProviderInterface(ABC):
    @abstractmethod
    def get_stock_current_price(self, symbol: str) -> Optional[float]:
        """Fetch the current price of a stock."""
        pass

    @abstractmethod
    def get_intraday_chart(self, symbol: str) -> List[StockChartSchema]:
        """Fetch intraday chart data for a stock."""
        pass

    @abstractmethod
    def get_historical_data(self, symbol: str) -> List[StockAllSchema]:
        """Fetch historical data for a stock."""
        pass
