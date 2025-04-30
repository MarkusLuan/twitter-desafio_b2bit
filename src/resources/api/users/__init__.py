from flask import Blueprint
import flask_restful as Rest

from . import routes

resources = Blueprint("users", __name__, url_prefix="/users")
api = Rest.Api(resources)
api.add_resource(routes.Users, "/")
api.add_resource(routes.UserInfo, "/<uuid:uuid_user>")