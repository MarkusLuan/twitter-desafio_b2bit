from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_basicauth import BasicAuth

db = SQLAlchemy()
migrate = Migrate()
basic_auth = BasicAuth()