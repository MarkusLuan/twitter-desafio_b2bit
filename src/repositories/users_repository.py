from .abstract_repository import AbstractRepository
from sqlalchemy import or_

from uuid import UUID

from models import User
import seguranca_utils
from exceptions import user_exceptions

class UsersRepository (AbstractRepository):
    @property
    def model(self):
        return User
    
    @property
    def __rand_hash(self):
        return "N2ppx5x0kd"
    
    def __hash_senha(self, senha: str):
        return seguranca_utils.hash(
            seguranca_utils.fromBase64(senha),
            self.__rand_hash
        )

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

        if not user or user.senha != self.__hash_senha(senha):
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
        
        _entity.senha = self.__hash_senha(_entity.senha)
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