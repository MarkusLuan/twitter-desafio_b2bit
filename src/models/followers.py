from sqlalchemy import Integer, ForeignKey, UniqueConstraint

from .abstract_model import AbstractModel
from app_singleton import db

class Followers (AbstractModel):
    seguidor_id = db.Column(Integer, ForeignKey("user.id"), nullable=False)
    seguindo_id = db.Column(Integer, ForeignKey("user.id"), nullable=False)

    seguidor = db.relationship("User", foreign_keys=[seguidor_id])
    seguindo = db.relationship("User", foreign_keys=[seguindo_id])

    __table_args__ = (
        UniqueConstraint('seguidor_id', 'seguindo_id', name="uix_follower_users"),
    )

    @property
    def json(self):
        j = super().json

        j["seguidor"] = self.seguidor.nick
        j["seguindo"] = self.seguindo.nick
        return j