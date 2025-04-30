import app

import os
import sys

PROJECT_DIR = "/app"

sys.path.insert(0, PROJECT_DIR)
os.chdir(PROJECT_DIR)

application = app.create_app("config.prod")