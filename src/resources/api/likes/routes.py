from flask import request, jsonify, abort

import uuid

from models import Likes as LikesModel
from repositories import FeedRepository, LikesRepository
from ..abstract_routes import AbstractRoutes
import app_singleton

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

        count = self.__repository.count_by_feed_uuid(uuid_feed)

        
        feed.count_likes = count
        self.__feed_repository.update(feed)

        return jsonify(like.json)
    
    def delete(self, uuid_feed: uuid.UUID):
        "Endpoint para descurtir uma postagem - Remoção fisica"

        return jsonify({})