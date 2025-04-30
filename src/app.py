from flask import Flask

from resources import resources
from error_handler import ErrorHandler

def create_app(config: str):
    app = Flask(__name__)

    app.config.from_object(config)
    app.register_blueprint(resources)
    ErrorHandler(app)

    return app

if __name__ == "__main__":
    app = create_app("config.dev")

    app.run(
        "0.0.0.0",
        80,
        True
    )