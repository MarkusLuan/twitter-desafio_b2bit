from flask import Blueprint

from . import api

resources = Blueprint(__name__, __name__)
resources.register_blueprint(api.resources)