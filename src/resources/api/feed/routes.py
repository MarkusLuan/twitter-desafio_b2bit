import datetime
from flask import request, jsonify, abort

import uuid

from models import Feed as FeedModel, Paginacao
from repositories import FeedRepository
import utils
from ..abstract_routes import AbstractRoutes
import app_singleton

class Feed (AbstractRoutes):
    __repository = FeedRepository()

    def get(self, uuid_feed: uuid.UUID=None):
        "Endpoint para carregar o feed do usuário logado"

        if uuid_feed:
            # Obtem informações do post
            feed = self.__repository.get_by_uuid(uuid_feed)
            if feed.user != self.logged_user:
                return abort(404)
            return jsonify(feed.json)

        self.__repository.paginacao = Paginacao(**request.args.to_dict())
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
    
    def put(self, uuid_feed: uuid.UUID):
        "Endpoint para editar uma postagem"

        # Garantir que seja passado um JSON
        if not request.is_json:
            return abort(400)
        
        j = request.json or {}
        utils.validar_campos_obrigatorios(j, [
            "texto"
        ])

        # Garantindo que apenas o usuario proprietário delete a postagem
        feed = self.__repository.get_by_uuid(uuid_feed)
        if feed.user != self.logged_user:
            return abort(404)
        
        feed.texto = j["texto"]
        self.__repository.update(feed)

        return jsonify(feed.json)
    
    def delete(self, uuid_feed: uuid.UUID):
        "Endpoint para apagar uma postagem - Remoção lógica"

        # Garantindo que apenas o usuario proprietário delete a postagem
        feed = self.__repository.get_by_uuid(uuid_feed)
        if feed.user != self.logged_user:
            return abort(404)
        
        deleted_feed= feed.json
        feed.dt_remocao = datetime.datetime.now()
        self.__repository.update(feed)

        return jsonify(deleted_feed)