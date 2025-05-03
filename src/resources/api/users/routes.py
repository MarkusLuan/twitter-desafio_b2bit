from flask import request, jsonify, abort
from werkzeug.exceptions import BadRequest

from repositories import UsersRepository
from models import User as UserModel
import utils
from ..abstract_routes import AbstractRoutes
import app_singleton

class Users (AbstractRoutes):
    __repository = UsersRepository()

    def get(self, nick: str=""):
        "Endpoint para pesquisar por usuario"
        
        # Retorna as informações de um usuario pelo nick
        if nick:
            user = self.__repository.get_by_nick(nick)
            return jsonify(user.json)

        # Pesquisa por um usuario
        j = request.args.to_dict()
        utils.validar_campos_obrigatorios(j, [
            "search"
        ])
        
        users = self.__repository.search_by_nick_ou_nome(
            j["search"],
            first_result=int(j.get("first_result", 0)),
            max_results=int(j.get("max_results", 0))
        )
        return jsonify(users)
    
    @app_singleton.basic_auth.required
    def post(self):
        "Endpoint para cadastrar usuário"

        # Garantir que seja passado um JSON
        if not request.is_json:
            return abort(400)
        
        j = request.json or {}
        utils.validar_campos_obrigatorios(j, [
            "dt_nascimento",
            "nick",
            "nome",
            "email",
            "bio",
            "senha",
        ])
        utils.remover_campos(j, ["id", "uuid", "dt_criacao"])
        
        user = self.__repository.insert(UserModel(**j))
        return jsonify(user.json)