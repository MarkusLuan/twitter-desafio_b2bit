from flask import request, jsonify, abort

import uuid

from ..abstract_routes import AbstractRoutes
import app_singleton

class Followers (AbstractRoutes):
    def get(self):
        "Endpoint para listar seguidores do usuário logado"

        return jsonify({})
    
    def post(self, uuid_user: uuid.UUID):
        "Endpoint para seguir um usuario"

        return jsonify({})
    
    def delete(self, uuid_user: uuid.UUID):
        "Endpoint para deixar de seguir um usuário - Remoção fisica"

        return jsonify({})