"""
This example is about downloading all tickers csv data.
"""

from ..download import download
from .. import download_client_types_records

download_client_types_records(symbols="all", write_to_csv=True,base_path="app\\download\\1")
download(symbols="all", write_to_csv=True, base_path="app\\download\\2")
