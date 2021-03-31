import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    toBeContinued = True

    @staticmethod
    def init_app(app):
        pass


class PreAlphaConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jose'
    DOWNLOAD_DIR = os.path.join(basedir, 'download')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # PROPAGATE_EXCEPTIONS = True


config = {
    'development': PreAlphaConfig,
    'testing': PreAlphaConfig,
    'production': PreAlphaConfig,
    'default': PreAlphaConfig
}
