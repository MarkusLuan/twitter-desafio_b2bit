from flask import Blueprint
from flask import request, jsonify, abort
import flask_jwt_extended as jwt

import datetime

from repositories import UsersRepository
import app_singleton

repository = UsersRepository()
resources = Blueprint("auth", __name__, url_prefix="/auth")

def gerar_token(identity):
    dt_agora = datetime.datetime.now()
    delta_expiracao = datetime.timedelta(hours=1)
    dt_expiracao = delta_expiracao + dt_agora
    
    res = {
        "created_at": dt_agora.timestamp(),
        "access_token": jwt.create_access_token(identity, expires_delta=delta_expiracao),
        "refresh_token": jwt.create_refresh_token(identity, delta_expiracao),
        "expires_in": dt_expiracao.timestamp()
    }
    
    return res

@resources.route("/token", methods=["POST"])
@app_singleton.basic_auth.required
def get_token():
    if not request.is_json:
        return abort(400)
    
    j = request.json or {}
    if "username" not in j or "senha" not in j:
        return abort(400)
    
    user = repository.fazer_login(
        j["username"], 
        j["senha"]
    )
    
    return jsonify(gerar_token(user.uuid))

@resources.route("/refresh", methods=["POST"])
@jwt.jwt_required(refresh=True)
def refresh_token():
    identity = jwt.get_jwt_identity()
    return jsonify(gerar_token(identity))