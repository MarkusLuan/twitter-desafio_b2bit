from .abstract_repository import AbstractRepository

from uuid import UUID

from models import Likes, Feed

class LikesRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        like = Likes.query.filter(
            Likes.uuid == str(_uuid)
        ).first()

        return like
    
    def get_by_feed_uuid(self, _feed_uuid: UUID):
        likes = Likes.query.join(
            Feed,
            Likes.feed_id == Feed.id
        ).filter(
            Feed.uuid == str(_feed_uuid)
        ).all()

        return likes
    
    def count_by_feed_uuid(self, _feed_uuid: UUID):
        likes = Likes.query.join(
            Feed,
            Likes.feed_id == Feed.id
        ).filter(
            Feed.uuid == str(_feed_uuid)
        ).count()

        return likes
    
    def update(self, _entity):
        ...

    def delete(self, _entity):
        ...