from flask import Flask

from resources import resources
from error_handler import ErrorHandler

app = Flask(__name__)
app.register_blueprint(resources)
ErrorHandler(app)

if __name__ == "__main__":
    app.config.from_object("config.dev")
    app.run(
        "0.0.0.0",
        80,
        True
    )