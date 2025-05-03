from flask import Blueprint
import flask_restful as Rest

from . import routes

resources = Blueprint("feed", __name__, url_prefix="/feed")
api = Rest.Api(resources)
api.add_resource(routes.Feed, "/", "/<string:uuid_feed>")
api.add_resource(routes.FeedImg, "/<string:uuid_feed>/img")