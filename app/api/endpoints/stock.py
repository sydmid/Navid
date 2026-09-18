from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import text, desc
from typing import List, Dict, Any
from datetime import datetime, timedelta
import importlib
from pydantic import TypeAdapter

from app.db import get_db
from app.schemas.stock import StockChartSchema, StockClientsSchema, StockAllSchema, StockGeneralSchema

router = APIRouter()

from app.storage.timeseries import read_stock_data, write_stock_data
from app.core.events import event_bus
import asyncio
from app.tset_client.provider import TSETMCProvider
from app.core.provider_interface import ProviderInterface

class GatewayProvider(ProviderInterface):
    def __init__(self, provider: ProviderInterface):
        self.provider = provider

    def get_stock_current_price(self, symbol: str) -> float | None:
        return self.provider.get_stock_current_price(symbol)

    def get_intraday_chart(self, symbol: str) -> List[StockChartSchema]:
        return self.provider.get_intraday_chart(symbol)

    def get_historical_data(self, symbol: str) -> List[StockAllSchema]:
        import pandas as pd
        df = read_stock_data(symbol)

        # If cache hit and data seems fresh enough
        if df is not None and not df.empty:
            records = []
            for row in df.itertuples():
                record_dict = row._asdict()
                clean_dict = {k: (v if pd.notna(v) else None) for k, v in record_dict.items() if k != 'Index'}
                if 'date' in clean_dict and isinstance(clean_dict['date'], pd.Timestamp):
                    clean_dict['date'] = clean_dict['date'].date()
                if 'jdate' in clean_dict:
                    clean_dict.pop('jdate')
                try:
                    records.append(StockAllSchema(**clean_dict))
                except Exception:
                    pass
            return records

        # Fallback to fetching new data
        records = self.provider.get_historical_data(symbol)
        if records:
            # Save the new data to cache
            records_dicts = [r.model_dump(mode='json') for r in records]
            new_df = pd.DataFrame(records_dicts)
            # convert date back to datetime for storage
            new_df['date'] = pd.to_datetime(new_df['date'])
            write_stock_data(symbol, new_df)

            # Emit event
            try:
                import anyio
                anyio.from_thread.run(event_bus.publish, f"market_data.tick.{symbol}", records_dicts)
            except Exception as e:
                print(f"Failed to emit event: {e}")

        return records

def get_market_data_provider() -> ProviderInterface:
    return GatewayProvider(TSETMCProvider())

marshmallows_dict = {
    'chart': StockChartSchema,
    'general-all': StockGeneralSchema,
    'clients-all': StockClientsSchema,
    'all': StockAllSchema
}


@router.get("/stock-t-span/{name}/y/{year_ago}/{mode}")
def get_stock_year(name: str, year_ago: int, mode: str, provider: ProviderInterface = Depends(get_market_data_provider)):
    target_date = (datetime.now() - timedelta(days=year_ago * 365)).date()
    records = provider.get_historical_data(name)
    records = [r for r in records if r.date and r.date >= target_date]
    if not records:
         return {name: '[]'}

    if mode not in marshmallows_dict:
        raise HTTPException(status_code=400, detail="Invalid mode")
    schema = marshmallows_dict[mode]
    adapter = TypeAdapter(List[schema])
    data = [m.model_dump(mode='json') for m in adapter.validate_python(records)]
    return {name: str(data).replace("'", '"')}

@router.get("/stock-t-span/{name}/m/{month_ago}/{mode}")
def get_stock_month(name: str, month_ago: int, mode: str, provider: ProviderInterface = Depends(get_market_data_provider)):
    target_date = (datetime.now() - timedelta(days=month_ago * 30)).date()
    records = provider.get_historical_data(name)
    records = [r for r in records if r.date and r.date >= target_date]
    if not records:
         return {name: '[]'}

    if mode not in marshmallows_dict:
        raise HTTPException(status_code=400, detail="Invalid mode")
    schema = marshmallows_dict[mode]
    adapter = TypeAdapter(List[schema])
    data = [m.model_dump(mode='json') for m in adapter.validate_python(records)]
    return {name: str(data).replace("'", '"')}

@router.get("/api/stock-t-span/{name}/y/{year_ago}/{mode}")
def get_stock_year_api(name: str, year_ago: int, mode: str, provider: ProviderInterface = Depends(get_market_data_provider)):
    target_date = (datetime.now() - timedelta(days=year_ago * 365)).date()
    records = provider.get_historical_data(name)
    records = [r for r in records if r.date and r.date >= target_date]
    if mode not in marshmallows_dict:
        raise HTTPException(status_code=400, detail="Invalid mode")
    schema = marshmallows_dict[mode]
    adapter = TypeAdapter(List[schema])
    return [m.model_dump(mode='json') for m in adapter.validate_python(records)]

@router.get("/api/stock-t-span/{name}/m/{month_ago}/{mode}")
def get_stock_month_api(name: str, month_ago: int, mode: str, provider: ProviderInterface = Depends(get_market_data_provider)):
    target_date = (datetime.now() - timedelta(days=month_ago * 30)).date()
    records = provider.get_historical_data(name)
    records = [r for r in records if r.date and r.date >= target_date]
    if mode not in marshmallows_dict:
        raise HTTPException(status_code=400, detail="Invalid mode")
    schema = marshmallows_dict[mode]
    adapter = TypeAdapter(List[schema])
    return [m.model_dump(mode='json') for m in adapter.validate_python(records)]

@router.get("/today/{name}")
def get_today_history(name: str, provider: ProviderInterface = Depends(get_market_data_provider)):
     target_date = (datetime.now() - timedelta(days=1)).date()
     records = provider.get_historical_data(name)
     records = [r for r in records if r.date and r.date >= target_date]
     schema = marshmallows_dict["all"]
     adapter = TypeAdapter(List[schema])
     data = [m.model_dump(mode='json') for m in adapter.validate_python(records)]
     return {"records": data}

