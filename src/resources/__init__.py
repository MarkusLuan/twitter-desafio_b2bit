from flask import Blueprint
from flask import request
import flask_jwt_extended as jwt

from . import api
import app_singleton

resources = Blueprint(__name__, __name__)
resources.register_blueprint(api.resources)

@resources.before_app_request
def before_request():
    if request.endpoint in ["resources.api.auth.get_token", "resources.api.auth.refresh_token"]:
        return
    
    if request.endpoint in ["users.users"] and request.method == "POST":
        return
    
    jwt.verify_jwt_in_request(False)