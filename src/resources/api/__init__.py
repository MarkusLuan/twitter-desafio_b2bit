from flask import Blueprint

from . import auth

resources = Blueprint("api", __name__, url_prefix="/api")
resources.register_blueprint(auth.resources)