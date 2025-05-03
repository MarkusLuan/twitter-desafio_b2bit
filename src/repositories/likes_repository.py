from .abstract_repository import AbstractRepository

from uuid import UUID

from models import Likes, Feed, User

class LikesRepository (AbstractRepository):
    @property
    def model(self):
        return Likes

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
    
    def get_by_feed_uuid_and_user_uuid(self, _feed_uuid: UUID, _user_uuid: UUID):
        like = Likes.query.join(
            Feed,
            Likes.feed_id == Feed.id
        ).join(
            User,
            User.id == Likes.user_id
        ).filter(
            Feed.uuid == str(_feed_uuid),
            User.uuid == str(_user_uuid)
        ).first()

        return like
    
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
        db_session = self.db_session
        db_session.delete(_entity)
        db_session.commit()