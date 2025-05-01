from flask import Flask

from resources import resources
from error_handler import ErrorHandler
import app_singleton

def create_app(config: str):
    _app = Flask(__name__)
    _app.config.from_object(config)

    if "DATABASE" in _app.config:
        db_config = _app.config["DATABASE"]
        db_uri = "{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}".format(
            **db_config
        )
        
        _app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
        _app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

    app_singleton.basic_auth.init_app(_app)

    app_singleton.db.init_app(_app)
    app_singleton.migrate.init_app(_app, app_singleton.db)

    _app.register_blueprint(resources)
    ErrorHandler(_app)

    return _app

if __name__ == "__main__":
    app = create_app("config.dev")

    app.run(
        "0.0.0.0",
        8050,
        True
    )