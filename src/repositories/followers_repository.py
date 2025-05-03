from .abstract_repository import AbstractRepository

from uuid import UUID

from models import Followers

class FollowersRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        follower = Followers.query.filter(
            Followers.uuid == str(_uuid)
        ).first()

        return follower
    
    def update(self, _entity):
        ...

    def delete(self, _entity):
        ...