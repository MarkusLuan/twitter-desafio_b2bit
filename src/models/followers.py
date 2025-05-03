from sqlalchemy import Integer, ForeignKey, UniqueConstraint

from .abstract_model import AbstractModel
from app_singleton import db

class Followers (AbstractModel):
    seguidor_id = db.Column(Integer, ForeignKey("user.id"), nullable=False)
    seguindo_id = db.Column(Integer, ForeignKey("user.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint('seguidor_id', 'seguindo_id', name="uix_follower_users"),
    )