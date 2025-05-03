from sqlalchemy import DateTime, Integer, ForeignKey

import os
import base64

from .abstract_model import AbstractModel
import constantes
from app_singleton import db

class Feed (AbstractModel):
    fields = ["texto", "count_likes", "is_liked", "img_src"]

    dt_remocao = db.Column(DateTime, nullable=True)
    texto = db.Column(db.String, nullable=False)
    count_likes = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(Integer, ForeignKey("user.id"), nullable=False)

    user = db.relationship("User")

    is_liked = False

    @property
    def img_path(self):
        return f"{constantes.FEED_IMG_PATH}/{self.uuid}.png"
    
    @property
    def has_image(self):
        return os.path.isfile(self.img_path)
    
    @property
    def img_src(self):
        blob = None
        if self.has_image:
            with open(self.img_path, "rb") as f:
                blob = base64.b64encode(f.read()).decode("utf-8")
        return blob
    
    @property
    def json(self):
        j = super().json

        j["created_by"] = self.user.nick
        return j