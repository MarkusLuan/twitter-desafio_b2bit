from flask import request, jsonify, abort
import flask_restful as Rest

import uuid

import app_singleton

class Likes (Rest.Resource):
    def get(self, uuid_feed: uuid.UUID):
        "Endpoint para listar curtidas por postagem"

        return jsonify({})
    
    def post(self, uuid_feed: uuid.UUID):
        "Endpoint para curtir uma postagem"

        return jsonify({})
    
    def delete(self, uuid_feed: uuid.UUID):
        "Endpoint para descurtir uma postagem - Remoção fisica"

        return jsonify({})