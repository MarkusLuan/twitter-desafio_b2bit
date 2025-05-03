from flask import Blueprint
import flask_restful as Rest

from . import routes

resources = Blueprint("followers", __name__, url_prefix="/followers")
api = Rest.Api(resources)
api.add_resource(routes.Followers, "/", "/<string:nick_user>")