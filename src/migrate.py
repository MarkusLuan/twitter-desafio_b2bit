import app
import app_singleton
from models import *

import argparse

def migrate(_config_object: str):
    _app = app.create_app(_config_object)

    with _app.app_context():
        app_singleton.db.drop_all()
        app_singleton.db.create_all()

if __name__ == "__main__":
    paser = argparse.ArgumentParser(exit_on_error=False)
    paser.add_argument("--config", default="config.dev")
    config_object = paser.parse_known_args()[0].config

    migrate(config_object)