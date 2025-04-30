from .abstract_repository import AbstractRepository

from uuid import UUID

from models import Feed
from exceptions import feed_exceptions

class FeedRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        feed = Feed.query.filter(
            Feed.uuid == _uuid
        ).first()

        if not feed:
            raise feed_exceptions.FeedNotFoundException()

        return feed