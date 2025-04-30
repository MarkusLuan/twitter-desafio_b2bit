from .abstract_repository import AbstractRepository
from sqlalchemy import or_

from uuid import UUID

from models import User

class UsersRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        return super().get_by_uuid(_uuid)
    
    def fazer_login(self, usuario: str, senha: str):
        user = User.query.filter(or_(
            User.nick == usuario,
            User.email == usuario
        )).first()

        if not user or user.senha != senha:
            raise Exception ("Erro")
        
        user.senha = None
        return user