from .abstract_repository import AbstractRepository

from uuid import UUID

class FollowersRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        return super().get_by_uuid(_uuid)