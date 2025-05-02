from .abstract_repository import AbstractRepository
from sqlalchemy import or_, Join

from uuid import UUID

from models import Feed, Followers, User
from exceptions import feed_exceptions

class FeedRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID):
        feed = Feed.query.filter(
            Feed.uuid == _uuid
        ).first()

        if not feed:
            raise feed_exceptions.FeedNotFoundException()

        return feed
    
    def get_by_user_uuid(self, _user_uuid: UUID):
        feeds = Feed.query.join(
                User,
                Feed.user_id == User.id
            ).outerjoin(
            Followers, 
            Feed.user_id == Followers.seguidor_id
            ).filter(
                User.uuid == _user_uuid
            ).order_by(Feed.dt_criacao).all()

        return feeds