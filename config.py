import os
from datetime import timedelta


class Config:
    toBeContinued = True

    # Optional for doing config[config_name].init_app(app) in the main factory
    @staticmethod
    def init_app(app):
        pass


class PreAlpha(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'javad'
    DOWNLOAD_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'download')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.db') + '?check_same_thread=False'
    # 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    # disables the flask_sqlachemy track modification not sqlalchemy itself
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # flask extensions like flask_jwt can raise their own exception and app will know their specific error
    PROPAGATE_EXCEPTIONS = True
    # We choose it to be different than app.secret_key (Optional)
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or \
        'mysecret1'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


config = {
    'development': PreAlpha,
    'testing': PreAlpha,
    'production': PreAlpha,
    'default': PreAlpha,
}
