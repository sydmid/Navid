import os
import asyncio
from app.utils import json_catalog_update
from app.utils import create_phase1_tables


def alternate_starter(toexecute):
    switcher = {
        'create_db_from_scratch': create_phase1_tables,
        'json_catalog_update': json_catalog_update
    }
    func_to_execute = switcher.get(toexecute, "dont have anything to execute")
    asyncio.run(func_to_execute())


alternate_starter(os.getenv('ALTERNATIVE_START'))
