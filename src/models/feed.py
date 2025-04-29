from sqlalchemy import DateTime, BigInteger, ForeignKey

import os

from .abstract_model import AbstractModel
from app_singleton import db

class Feed (AbstractModel):
    fields = []

    dt_remocao = db.Column(DateTime, nullable=True)
    texto = db.Column(db.String, nullable=False)
    count_likes = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)

    user = db.relationship("User")

    @property
    def img_path(self):
        return f"feed_img/{self.uuid}.png"
    
    @property
    def has_image(self):
        return os.path.isfile(self.img_path)
    
    @property
    def json(self):
        j = super().json

        j["created_by"] = self.user.nick
        return j