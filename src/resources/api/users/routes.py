from flask import request, jsonify, abort
import flask_restful as Rest

import uuid

import app_singleton

class Users (Rest.Resource):
    def get(self):
        "Endpoint para pesquisar por usuario"

        return jsonify({})
    
    def post(self):
        "Endpoint para cadastrar usuário"

        return jsonify({})

class UserInfo (Rest.Resource):
    def get(self, uuid_user: uuid.UUID):
        "Endpoint para mostrar informações do usuário"

        return jsonify({})