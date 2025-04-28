from flask import Flask

from resources import resources

app = Flask(__name__)
app.register_blueprint(resources)

if __name__ == "__main__":
    app.run(
        "0.0.0.0",
        80,
        True
    )