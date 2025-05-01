from sqlalchemy import Date

from .abstract_model import AbstractModel
from app_singleton import db

class User (AbstractModel):
    fields = ["dt_nascimento", "nome", "nick", "bio", "count_seguidores", "count_seguindo"]

    dt_nascimento = db.Column(Date, nullable=False)
    nome = db.Column(db.String, nullable=False)
    nick = db.Column(db.String, unique=True, nullable=False)
    bio = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)
    count_seguidores = db.Column(db.Integer, default=0, nullable=False)
    count_seguindo = db.Column(db.Integer, default=0, nullable=False)

    @property
    def json(self):
        j = super().json

        j["dt_nascimento"] = self.dt_nascimento.isoformat()
        return j