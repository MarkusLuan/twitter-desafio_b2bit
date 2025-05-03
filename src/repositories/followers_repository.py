from .abstract_repository import AbstractRepository
from sqlalchemy import and_

from uuid import UUID

from models import Followers
from exceptions import follower_exceptions

class FollowersRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        follower = Followers.query.filter(
            Followers.uuid == str(_uuid)
        ).first()

        return follower
    
    def get(self, seguidor_id: int, seguindo_id: int):
        follower = Followers.query.filter(and_(
            Followers.seguidor_id == seguidor_id,
            Followers.seguindo_id == seguindo_id,
        )).first()

        if not follower:
            raise follower_exceptions.FollowerNotFoundException()

        return follower
    
    def count_seguidores_by_user_id(self, user_id: int):
        count_seguidores = Followers.query.filter(
            Followers.seguindo_id == user_id
        ).count()

        return count_seguidores
    
    def count_seguindo_by_user_id(self, user_id: int):
        count_seguindo = Followers.query.filter(
            Followers.seguidor_id == user_id
        ).count()

        return count_seguindo

    def update(self, _entity):
        ...

    def delete(self, _entity):
        db= self.db_session
        db.delete(_entity)
        db.commit()

        return _entity