from flask import Blueprint
import flask_restful as Rest

from . import routes

resources = Blueprint("likes", __name__, url_prefix="/likes")
api = Rest.Api(resources)
api.add_resource(routes.Likes, "/<uuid:uuid_feed>")