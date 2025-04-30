from flask import request, jsonify, abort
import flask_restful as Rest

import uuid

import app_singleton

class Feed (Rest.Resource):
    def get(self):
        "Endpoint para carregar o feed do usuário logado"

        return jsonify({})
    
    def post(self):
        "Endpoint para criar uma postagem"

        return jsonify({})
    
    def delete(self, uuid_feed: uuid.UUID):
        "Endpoint para apagar (por tag) uma postagem"

        return jsonify({})