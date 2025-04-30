from .abstract_repository import AbstractRepository

from uuid import UUID

class FeedRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        return super().get_by_uuid(_uuid)