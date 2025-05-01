import app
import app_singleton
from models import *

import sys
import argparse

paser = argparse.ArgumentParser(exit_on_error=False)
paser.add_argument("--config", default="config.dev")

config_object = paser.parse_known_args()[0].config
print (config_object)
app = app.create_app(config_object)

with app.app_context():
    app_singleton.db.drop_all()
    app_singleton.db.create_all()