from flask import request, jsonify, abort

import uuid

from ..abstract_routes import AbstractRoutes
from repositories import FollowersRepository, UsersRepository
from models import Followers as FollowersModel
from exceptions import follower_exceptions
import app_singleton

class Followers (AbstractRoutes):
    __repository = FollowersRepository()
    __users_repository = UsersRepository()

    def get(self):
        "Endpoint para listar seguidores do usuário logado"

        return jsonify({})
    
    def post(self, nick_user: str):
        "Endpoint para seguir um usuario"
        
        logged_user = self.logged_user
        if logged_user is None or logged_user.nick == nick_user:
            raise follower_exceptions.FollowerInvalidException()
        
        user = self.__users_repository.get_by_nick(nick_user)
        follower = self.__repository.insert(FollowersModel(
            seguidor_id = logged_user.id,
            seguindo_id = user.id
        ))

        # TODO: Implementar atualização de cache
        user.count_seguidores = 0
        logged_user.count_seguindo = 0
        self.__users_repository.update(user)
        self.__users_repository.update(logged_user)

        return jsonify(follower.json)
    
    def delete(self, nick_user: str):
        "Endpoint para deixar de seguir um usuário - Remoção fisica"

        logged_user = self.logged_user
        if logged_user is None or logged_user.nick == nick_user:
            raise follower_exceptions.FollowerInvalidException()
        
        user = self.__users_repository.get_by_nick(nick_user)
        follower = self.__repository.get(logged_user.id, user.id)
        deleted_follower = follower.json
        self.__repository.delete(follower)

        # TODO: Implementar atualização de cache
        user.count_seguidores = 0
        logged_user.count_seguindo = 0
        self.__users_repository.update(user)
        self.__users_repository.update(logged_user)

        return jsonify(deleted_follower)