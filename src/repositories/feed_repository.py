from .abstract_repository import AbstractRepository
from sqlalchemy import desc, and_, or_

from uuid import UUID

from models import Feed, Followers, User, Likes
from exceptions import feed_exceptions

class FeedRepository (AbstractRepository):
    def get_by_uuid(self, _uuid: UUID) -> Feed:
        feed = Feed.query.filter(
            Feed.uuid == str(_uuid),
            Feed.dt_remocao.is_(None)
        ).first()

        if not feed:
            raise feed_exceptions.FeedNotFoundException()

        return feed
    
    def subquery_is_liked_by_user(self, db_session, _user_uuid: UUID):
       return db_session.query(Likes.id).join(
            User,
            User.id == Likes.user_id
        ).filter(
            Likes.feed_id == Feed.id,
            User.uuid == str(_user_uuid)
        ).correlate(Feed).exists()
    
    def get_by_user_uuid(self, _user_uuid: UUID):
        db_session = self.db_session
        subq_is_liked_by_user = self.subquery_is_liked_by_user(
            db_session, 
            _user_uuid
        )

        query = db_session.query(
            Feed,
            subq_is_liked_by_user.label("is_liked")
        ).outerjoin(
            Followers, 
            Followers.seguindo_id == Feed.user_id
        ).join(
            User,
            or_(
                Feed.user_id == User.id,
                Followers.seguidor_id == User.id
            )
        ).filter(
            User.uuid == str(_user_uuid),
            Feed.dt_remocao.is_(None)
        ).order_by(desc(
            Feed.dt_criacao
        ))

        query = self.paginate(query)
        res = query.all()
        
        feeds = []
        for feed, is_liked in res:
            feed.is_liked = is_liked
            feeds.append(feed)

        return feeds
    
    def update(self, _entity):
        db = self.db_session
        Feed.query.filter(Feed.id == _entity.id).update({
            Feed.dt_remocao: _entity.dt_remocao,
            Feed.texto: _entity.texto,
            Feed.count_likes: _entity.count_likes,
        })
        db.commit()

    def delete(self, _entity):
        ...