from flask import Blueprint

from . import auth, users, feed, followers

resources = Blueprint("api", __name__, url_prefix="/api")
resources.register_blueprint(auth.resources)
resources.register_blueprint(users.resources)
resources.register_blueprint(feed.resources)
resources.register_blueprint(followers.resources)