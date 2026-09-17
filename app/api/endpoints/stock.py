from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import text, desc
from typing import List, Dict, Any
from datetime import datetime, timedelta
import importlib
from pydantic import TypeAdapter

from app.db import get_stocks_db, get_today_chart_db
from app.models.stocks import Stocks
from app.schemas.stock import StockChartSchema, StockClientsSchema, StockAllSchema, StockGeneralSchema

router = APIRouter()

marshmallows_dict = {
    'chart': StockChartSchema,
    'general-all': StockGeneralSchema,
    'clients-all': StockClientsSchema,
    'all': StockAllSchema
}

def dynamic_model_query(model_name: str, db: Session, date: datetime, mode: str):
    try:
        module = importlib.import_module("app.models.stock.stocks")
        model_class = getattr(module, model_name, None)
    except Exception:
        model_class = None

    if not model_class:
        try:
            module = importlib.import_module("app.models.today.all")
            model_class = getattr(module, f"امروز{model_name}", None)
            if not model_class:
                 model_class = getattr(module, model_name, None)
        except Exception:
            model_class = None

    if not model_class:
         raise HTTPException(status_code=404, detail="Stock model not found")

    try:
        if hasattr(model_class, 'date'):
             records = db.query(model_class).filter(model_class.date >= date.date()).all()
        elif hasattr(model_class, 'time'):
             records = db.query(model_class).filter(model_class.time >= date).all()
        else:
             records = db.query(model_class).all()
        return records
    except Exception as e:
        print(f"Query error: {e}")
        return []

@router.get("/stock-t-span/{name}/y/{year_ago}/{mode}")
def get_stock_year(name: str, year_ago: int, mode: str, db: Session = Depends(get_stocks_db)):
    date = datetime.now() - timedelta(days=year_ago * 365)
    records = dynamic_model_query(name, db, date, mode)
    if not records:
         return {name: '[]'}

    if mode not in marshmallows_dict:
        raise HTTPException(status_code=400, detail="Invalid mode")
    schema = marshmallows_dict[mode]
    adapter = TypeAdapter(List[schema])
    # The original app literally stringified a list of dicts here due to Flask legacy choices.
    # To preserve frontend expectations:
    data = [m.model_dump(mode='json') for m in adapter.validate_python(records)]
    return {name: str(data).replace("'", '"')}

@router.get("/stock-t-span/{name}/m/{month_ago}/{mode}")
def get_stock_month(name: str, month_ago: int, mode: str, db: Session = Depends(get_stocks_db)):
    date = datetime.now() - timedelta(days=month_ago * 30)
    records = dynamic_model_query(name, db, date, mode)
    if not records:
         return {name: '[]'}

    if mode not in marshmallows_dict:
        raise HTTPException(status_code=400, detail="Invalid mode")
    schema = marshmallows_dict[mode]
    adapter = TypeAdapter(List[schema])
    data = [m.model_dump(mode='json') for m in adapter.validate_python(records)]
    return {name: str(data).replace("'", '"')}

@router.get("/api/stock-t-span/{name}/y/{year_ago}/{mode}")
def get_stock_year_api(name: str, year_ago: int, mode: str, db: Session = Depends(get_stocks_db)):
    date = datetime.now() - timedelta(days=year_ago * 365)
    records = dynamic_model_query(name, db, date, mode)
    if mode not in marshmallows_dict:
        raise HTTPException(status_code=400, detail="Invalid mode")
    schema = marshmallows_dict[mode]
    adapter = TypeAdapter(List[schema])
    return [m.model_dump(mode='json') for m in adapter.validate_python(records)]

@router.get("/api/stock-t-span/{name}/m/{month_ago}/{mode}")
def get_stock_month_api(name: str, month_ago: int, mode: str, db: Session = Depends(get_stocks_db)):
    date = datetime.now() - timedelta(days=month_ago * 30)
    records = dynamic_model_query(name, db, date, mode)
    if mode not in marshmallows_dict:
        raise HTTPException(status_code=400, detail="Invalid mode")
    schema = marshmallows_dict[mode]
    adapter = TypeAdapter(List[schema])
    return [m.model_dump(mode='json') for m in adapter.validate_python(records)]

@router.get("/stocks-list")
def get_stocks_list(db: Session = Depends(get_stocks_db)):
    stocks = db.query(Stocks).all()
    return [{"name": s.name} for s in stocks]

@router.get("/today/{name}")
def get_today_history(name: str, db: Session = Depends(get_today_chart_db)):
     records = dynamic_model_query(name, db, datetime.now() - timedelta(days=1), "all")
     schema = marshmallows_dict["all"]
     adapter = TypeAdapter(List[schema])
     data = [m.model_dump(mode='json') for m in adapter.validate_python(records)]
     return {"records": data}

@router.post("/stock-utils")
def post_stock_utils(stock_name: List[str] = Query(...), job: str = Query(...), db: Session = Depends(get_stocks_db)):
    if job == "full-update":
        from app.tset_client import Downloader
        downloader = Downloader()
        downloaded = downloader.update_existing_db()
        import pandas as pd
        merged_stocks_object = {}
        all_stock_rows = {}
        counted_stocks_1 = {}
        counted_stocks_2 = {}
        for download_category, download_results in downloaded.items():
            if download_category == 'download-general':
                for stock_n, dataframe in download_results.items():
                    stock_n = str(stock_n).replace('ك', 'ک').replace('ي', 'ی').strip()
                    merged_stocks_object[stock_n] = []
                    df = pd.DataFrame(dataframe)
                    row_counter = 0
                    for row in df.itertuples():
                        merged_stocks_object[stock_n].append({})
                        merged_stocks_object[stock_n][row_counter]['name'] = stock_n
                        merged_stocks_object[stock_n][row_counter]['date'] = row.date
                        merged_stocks_object[stock_n][row_counter]['open'] = row.open
                        merged_stocks_object[stock_n][row_counter]['high'] = row.high
                        merged_stocks_object[stock_n][row_counter]['low'] = row.low
                        merged_stocks_object[stock_n][row_counter]['adjClose'] = row.adjClose
                        merged_stocks_object[stock_n][row_counter]['value'] = row.value
                        merged_stocks_object[stock_n][row_counter]['volume'] = row.volume
                        merged_stocks_object[stock_n][row_counter]['count'] = row.count
                        merged_stocks_object[stock_n][row_counter]['close'] = row.close
                        row_counter += 1
                    all_stock_rows[stock_n] = row_counter
            elif download_category == 'download-clients':
                for stock_n, dataframe in download_results.items():
                    stock_n = str(stock_n).replace('ك', 'ک').replace('ي', 'ی').strip()
                    df = pd.DataFrame(dataframe)
                    if stock_n not in all_stock_rows: continue
                    row_counter = all_stock_rows[stock_n] - 1
                    for row in df.itertuples():
                        if row_counter < 0 or row_counter >= len(merged_stocks_object.get(stock_n, [])): continue
                        merged_stocks_object[stock_n][row_counter]['individual_buy_count'] = getattr(row, 'individual_buy_count', None)
                        merged_stocks_object[stock_n][row_counter]['individual_sell_count'] = getattr(row, 'individual_sell_count', None)
                        merged_stocks_object[stock_n][row_counter]['individual_buy_vol'] = getattr(row, 'individual_buy_vol', None)
                        merged_stocks_object[stock_n][row_counter]['individual_sell_vol'] = getattr(row, 'individual_sell_vol', None)
                        merged_stocks_object[stock_n][row_counter]['individual_buy_value'] = getattr(row, 'individual_buy_value', None)
                        merged_stocks_object[stock_n][row_counter]['individual_sell_value'] = getattr(row, 'individual_sell_value', None)
                        merged_stocks_object[stock_n][row_counter]['corporate_buy_count'] = getattr(row, 'corporate_buy_count', None)
                        merged_stocks_object[stock_n][row_counter]['corporate_sell_count'] = getattr(row, 'corporate_sell_count', None)
                        merged_stocks_object[stock_n][row_counter]['corporate_buy_vol'] = getattr(row, 'corporate_buy_vol', None)
                        merged_stocks_object[stock_n][row_counter]['corporate_sell_vol'] = getattr(row, 'corporate_sell_vol', None)
                        merged_stocks_object[stock_n][row_counter]['corporate_buy_value'] = getattr(row, 'corporate_buy_value', None)
                        merged_stocks_object[stock_n][row_counter]['corporate_sell_value'] = getattr(row, 'corporate_sell_value', None)
                        merged_stocks_object[stock_n][row_counter]['individual_buy_mean_price'] = getattr(row, 'individual_buy_mean_price', None)
                        merged_stocks_object[stock_n][row_counter]['individual_sell_mean_price'] = getattr(row, 'individual_sell_mean_price', None)
                        merged_stocks_object[stock_n][row_counter]['corporate_buy_mean_price'] = getattr(row, 'corporate_buy_mean_price', None)
                        merged_stocks_object[stock_n][row_counter]['corporate_sell_mean_price'] = getattr(row, 'corporate_sell_mean_price', None)
                        merged_stocks_object[stock_n][row_counter]['individual_ownership_change'] = getattr(row, 'individual_ownership_change', None)
                        if row_counter != 0:
                            row_counter -= 1

        tables = []
        import app.models.stock.stocks as stocks_module
        for stock_n, stockrecords in merged_stocks_object.items():
            stock_n = str.replace(stock_n,'\u200c', '')
            stock_n = str.replace(stock_n,' ', '')
            record_class = getattr(stocks_module, stock_n, None)
            if not record_class: continue

            try:
                # Retrieve last record date using SQLAlchemy since find_last_date is removed
                last_record = db.query(record_class).order_by(desc(record_class.date)).first()
                date = last_record.date if last_record else None
            except:
                date = None

            if date is not None:
                existing_date = date
                for record in stockrecords:
                    if record['date'] <= existing_date:
                        continue
                    tables.append(record_class(**record))
            else:
                for record in stockrecords:
                    tables.append(record_class(**record))
        db.add_all(tables)
        db.commit()

    return {"message": f"{job} Done."}
