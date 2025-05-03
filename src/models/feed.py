from sqlalchemy import DateTime, Integer, ForeignKey

import os

from .abstract_model import AbstractModel
from app_singleton import db

class Feed (AbstractModel):
    fields = ["texto", "count_likes", "is_liked"]

    dt_remocao = db.Column(DateTime, nullable=True)
    texto = db.Column(db.String, nullable=False)
    count_likes = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(Integer, ForeignKey("user.id"), nullable=False)

    user = db.relationship("User")

    is_liked = False

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