import os
from app.utils.stock_info import json_catalog_update
from app.utils.create_tables import create_tset_tables
import asyncio


def function_switcher(toexecute):
    switcher = {
        'create_db_from_scratch': create_tset_tables,
        'json_catalog_update': json_catalog_update
    }
    func_to_execute = switcher.get(toexecute, "dont have anything to execute")
    asyncio.run(func_to_execute())


function_switcher(os.getenv('ALTERNATIVE_START'))
