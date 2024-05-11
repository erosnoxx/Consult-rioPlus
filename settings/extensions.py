from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mailman import Mail
from flask_restx import Api
from flask_caching import Cache

db = SQLAlchemy()
lm = LoginManager()
mail = Mail()
api = Api(prefix='/api/v1/', doc='/api/v1/docs/')
cache = Cache()

def init_app(app) -> None:
    db.init_app(app)
    Migrate(app, db)