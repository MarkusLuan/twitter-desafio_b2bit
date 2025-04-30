from flask import Blueprint
from flask import request, jsonify, abort

import app_singleton

resources = Blueprint("auth", __name__, url_prefix="/auth")

@resources.route("/token", methods=["POST"])
@app_singleton.basic_auth.required
def get_token():
    if not request.is_json:
        return abort(400)
    
    j = request.json or {}
    
    return jsonify(j)

@resources.route("/refresh", methods=["POST"])
def refresh_token():
    if not request.is_json:
        return abort(400)
    
    j = request.json or {}
    
    return jsonify(j)