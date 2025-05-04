from flask import request, jsonify, abort

import os
import uuid
import datetime

from models import Feed as FeedModel, Paginacao
from repositories import FeedRepository
import utils
from ..abstract_routes import AbstractRoutes
import constantes

class Feed (AbstractRoutes):
    __repository = FeedRepository()

    def __salvar_img(self, uuid_feed: uuid.UUID, file):
        if not os.path.isdir(constantes.FEED_IMG_PATH):
            os.mkdir(constantes.FEED_IMG_PATH)
        
        file.save(f"{constantes.FEED_IMG_PATH}/{uuid_feed}.png")

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
        user = self.logged_user
        
        j = request.get_json() if request.is_json else request.form.to_dict()
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

        feed = FeedModel(**j)
        feed.uuid = uuid.uuid4()
        if "img" in request.files:
            self.__salvar_img(feed.uuid, request.files["img"])

        feed = self.__repository.insert(feed)
        return jsonify(feed.json)
    
    def put(self, uuid_feed: uuid.UUID):
        "Endpoint para editar uma postagem"

        j = request.get_json() if request.is_json else request.form.to_dict()
        utils.validar_campos_obrigatorios(j, [
            "texto"
        ])

        # Garantindo que apenas o usuario proprietário edite a postagem
        feed = self.__repository.get_by_uuid(uuid_feed)
        if feed.user != self.logged_user:
            return abort(404)
        
        feed.texto = j["texto"]
        if "img" in request.files:
            self.__salvar_img(uuid_feed, request.files["img"])

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
    
class FeedImg (AbstractRoutes):
    __repository = FeedRepository()

    def get(self, uuid_feed: uuid.UUID):
        "Endpoint para carregar imagem do feed"

        # Obtem informações do post
        feed = self.__repository.get_by_uuid(uuid_feed)
        if not feed.has_image:
            return abort(404)

        return feed.img_src