from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from . import views, errors

db = SQLAlchemy()

main = Blueprint('main', __name__)


