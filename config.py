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
    # disables the flask_sqlachemy track modification not sqlalchemy itself
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # flask extensions like flask_jwt can raise their own exception and app will know their specific error
    PROPAGATE_EXCEPTIONS = True
    # We choose it to be different than app.secret_key (Optional)
    JWT_SECRET_KEY = 'jose2'


config = {
    'development': PreAlphaConfig,
    'testing': PreAlphaConfig,
    'production': PreAlphaConfig,
    'default': PreAlphaConfig
}
