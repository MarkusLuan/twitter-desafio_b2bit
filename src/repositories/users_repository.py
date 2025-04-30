from .abstract_repository import AbstractRepository
from sqlalchemy import or_

from uuid import UUID

from models import User
from exceptions import user_exceptions

class UsersRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        user = User.query.filter(
            User.uuid == _uuid
        ).first()

        if not user:
            raise user_exceptions.UserNotFoundException()

        return user
    
    def fazer_login(self, usuario: str, senha: str):
        user = User.query.filter(or_(
            User.nick == usuario,
            User.email == usuario
        )).first()

        if not user or user.senha != senha:
            raise user_exceptions.InvalidLoginException()
        
        user.senha = None
        return user