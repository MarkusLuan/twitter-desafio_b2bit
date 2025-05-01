from flask import request, jsonify, abort
import flask_restful as Rest

import uuid

from repositories import UsersRepository
from models import User
import app_singleton

repository = UsersRepository()

class Users (Rest.Resource):
    def get(self):
        "Endpoint para pesquisar por usuario"

        return jsonify({})
    
    @app_singleton.basic_auth.required
    def post(self):
        "Endpoint para cadastrar usuário"

        # Garantir que seja passado um JSON
        if not request.is_json:
            return abort(400)
        
        j = request.json or {}
        user = repository.insert(User(**j))

        return jsonify(user.json)

class UserInfo (Rest.Resource):
    def get(self, uuid_user: uuid.UUID):
        "Endpoint para mostrar informações do usuário"

        return jsonify({})