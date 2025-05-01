from .abstract_repository import AbstractRepository

from uuid import UUID

from models import Likes

class LikesRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        like = Likes.query.filter(
            Likes.uuid == _uuid
        ).first()

        return like