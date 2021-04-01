import os
from app.main import create_app
from app.tset_client import download
from app.tset_client import download_client_types_records
from app.tset_client import controlled_download

# download_client_types_records('فولاد', write_to_csv=True,base_path="app\\download\\1")
# download("فولاد", write_to_csv=True, base_path="app\\download\\2")

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    # pass
    # controlled_download()
    app.run(port=5000, debug=True)
