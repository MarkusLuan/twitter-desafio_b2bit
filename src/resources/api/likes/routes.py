from flask import request, jsonify, abort

import uuid

from models import Likes as LikesModel
from repositories import FeedRepository, LikesRepository
from ..abstract_routes import AbstractRoutes

class Likes (AbstractRoutes):
    __repository = LikesRepository()
    __feed_repository = FeedRepository()

    def get(self, uuid_feed: uuid.UUID):
        "Endpoint para listar curtidas por postagem"

        likes = self.__repository.get_by_feed_uuid(uuid_feed)
        return jsonify([ like.json for like in likes ])
    
    def post(self, uuid_feed: uuid.UUID):
        "Endpoint para curtir uma postagem"
        
        user = self.logged_user
        feed = self.__feed_repository.get_by_uuid(uuid_feed)

        like = self.__repository.insert(LikesModel(**{
            "user_id": user.id,
            "feed_id": feed.id,
        }))

        feed.count_likes = self.__repository.count_by_feed_uuid(uuid_feed)
        self.__feed_repository.update(feed)

        return jsonify(like.json)
    
    def delete(self, uuid_feed: uuid.UUID):
        "Endpoint para descurtir uma postagem - Remoção fisica"

        like = self.__repository.get_by_feed_uuid_and_user_uuid(
            uuid_feed, 
            self.logged_user_uuid
        )

        if not like:
            return abort(404)
        
        deleted_like = like.json
        self.__repository.delete(like)

        # Atualiza cache de likes
        feed = self.__feed_repository.get_by_uuid(uuid_feed)
        feed.count_likes = self.__repository.count_by_feed_uuid(uuid_feed)
        self.__feed_repository.update(feed)

        return jsonify(deleted_like)