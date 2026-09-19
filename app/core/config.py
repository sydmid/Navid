from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os
from typing import Dict

class Settings(BaseSettings):
    ARCTICDB_URI: str = Field(default='lmdb://./arctic_db', env='ARCTICDB_URI')
    DEBUG: bool = True
    SECRET_KEY: str = Field(default='javad', env='SECRET_KEY')
    JWT_SECRET_KEY: str = Field(default='mysecret1', env='JWT_SECRET_KEY')
    DOWNLOAD_DIR: str = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'download')

    DEV_DATABASE_URL: str = Field(
        default='sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'test.db'),
        env='DEV_DATABASE_URL'
    )

    SQLALCHEMY_BINDS: Dict[str, str] = {
        'stocks_dict': f"sqlite:///{os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'sdict.db')}",
        'today_chart': f"sqlite:///{os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'today.db')}",
    }

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

settings = Settings()
