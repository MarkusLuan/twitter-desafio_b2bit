from flask import request, jsonify, abort
import flask_restful as Rest
import flask_jwt_extended as jwt

import uuid

from models import Feed as FeedModel
from repositories import FeedRepository, UsersRepository
import utils
import app_singleton

class Feed (Rest.Resource):
    __repository = FeedRepository()
    __users_repository = UsersRepository()

    def get(self):
        "Endpoint para carregar o feed do usuário logado"

        return jsonify({})
    
    def post(self):
        "Endpoint para criar uma postagem"
        # Garantir que seja passado um JSON
        if not request.is_json:
            return abort(400)
        
        uuid_user = jwt.get_jwt_identity()
        user = self.__users_repository.get_by_uuid(uuid_user)
        
        j = request.json or {}
        utils.validar_campos_obrigatorios(j, [
            "texto"
        ])
        utils.remover_campos(j, [
            "dt_remocao",
            "count_likes",
            "user_id",
            "user"
        ])
        j["user_id"] = user.id

        feed = self.__repository.insert(FeedModel(**j))
        return jsonify(feed.json)
    
    def delete(self, uuid_feed: uuid.UUID):
        "Endpoint para apagar uma postagem - Remoção lógica"

        return jsonify({})