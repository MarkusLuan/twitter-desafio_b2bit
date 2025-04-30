from sqlalchemy import BigInteger, DateTime, sql

import uuid

from app_singleton import db

class AbstractModel (db.Model):
    __abstract__ = True
    fields = []
    
    id = db.Column(BigInteger, primary_key=True)
    uuid = db.Column(db.String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    dt_criacao = db.Column(DateTime, default=sql.func.now(), nullable=False)

    @property
    def json(self):
        """ Serializer """
        
        j = {
            "uuid": str(self.uuid),
            "dt_criacao": self.dt_criacao.isoformat()
        }
        
        j.update({field: self.__getattribute__(field) for field in self.fields})
        
        return j
