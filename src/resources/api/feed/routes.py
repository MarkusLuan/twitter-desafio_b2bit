from flask import request, jsonify, abort

import uuid

from models import Feed as FeedModel
from repositories import FeedRepository
import utils
from ..abstract_routes import AbstractRoutes
import app_singleton

class Feed (AbstractRoutes):
    __repository = FeedRepository()

    def get(self):
        "Endpoint para carregar o feed do usuário logado"

        feeds = self.__repository.get_by_user_uuid(self.logged_user_uuid)
        return jsonify([ feed.json for feed in feeds])
    
    def post(self):
        "Endpoint para criar uma postagem"
        # Garantir que seja passado um JSON
        if not request.is_json:
            return abort(400)
        
        user = self.logged_user
        
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