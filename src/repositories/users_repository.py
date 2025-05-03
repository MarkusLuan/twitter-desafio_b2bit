from .abstract_repository import AbstractRepository
from sqlalchemy import or_

from uuid import UUID

from models import User
from exceptions import user_exceptions
import app_singleton

class UsersRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        user = User.query.filter(
            User.uuid == str(_uuid)
        ).first()

        if not user:
            raise user_exceptions.UserNotFoundException()

        return user
    
    def get_by_nick(self, nick: str):
        user = User.query.filter(
            User.nick == nick
        ).first()

        if not user:
            raise user_exceptions.UserNotFoundException()

        return user
    
    def search_by_nick_ou_nome(self, search: str):
        query = User.query.filter(or_(
            User.nick.ilike(f'%{search.lower()}%'),
            User.nome.ilike(f"%{search.lower()}%")
        ))

        query = self.paginate(query)
        users = query.all()
        return [user.json for user in users]
    
    def fazer_login(self, usuario: str, senha: str):
        user = User.query.filter(or_(
            User.nick == usuario,
            User.email == usuario
        )).first()

        if not user or user.senha != senha:
            raise user_exceptions.InvalidLoginException()
        
        user.senha = None
        return user
    
    def insert(self, _entity: User):
        user = User.query.filter(or_(
            User.nick == _entity.nick,
            User.email == _entity.email
        )).first()

        if user:
            raise user_exceptions.UserAlreadyRegisteredException()

        return super().insert(_entity)
    
    def update(self, _entity):
        db = self.db_session
        User.query.filter(User.id == _entity.id).update({
            User.bio: _entity.bio,
            User.count_seguidores : _entity.count_seguidores,
            User.count_seguindo : _entity.count_seguindo
        })
        db.commit()

        return _entity

    def delete(self, _entity):
        ...