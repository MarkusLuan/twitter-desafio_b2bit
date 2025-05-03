from sqlalchemy import Integer, ForeignKey, UniqueConstraint

from .abstract_model import AbstractModel
from app_singleton import db

class Likes (AbstractModel):
    user_id = db.Column(Integer, ForeignKey("user.id"), nullable=False)
    feed_id = db.Column(Integer, ForeignKey("feed.id"), nullable=False)
    
    user = db.relationship("User", foreign_keys=[user_id])
    feed = db.relationship("Feed", foreign_keys=[feed_id])

    __table_args__ = (
        UniqueConstraint('user_id', 'feed_id', name='uix_user_feed'),
    )

    @property
    def json(self):
        j = super().json

        j["liked_by"] = self.user.nick

        return j