from sqlalchemy import between
from sqlalchemy.orm import Query

from abc import ABC, abstractmethod
import uuid

from models import Paginacao
from models.abstract_model import AbstractModel
import app_singleton

class AbstractRepository (ABC):
    paginacao = Paginacao()
    
    @property
    @abstractmethod
    def model(self) -> AbstractModel:
        ...

    @property
    def db_session(self):
        return app_singleton.db.session

    @abstractmethod
    def get_by_uuid(self, _uuid: uuid.UUID):
        ...
    
    def insert(self, _entity):
        db= self.db_session
        db.add(_entity)
        db.commit()

        return _entity
    
    @abstractmethod
    def delete(self, _entity):
        ...
    
    @abstractmethod
    def update(self, _entity):
        ...

    def paginate(self, query: Query):
        """ Função reservada para fazer a paginação """

        query = query.offset(self.paginacao.first_result)
        if self.paginacao.max_results > 0:
            query = query.limit(self.paginacao.max_results)
        
        if self.paginacao.ts_after > 0:
            if self.paginacao.ts_before > 0:
                query = query.filter(
                    between(
                        self.model.dt_criacao,
                        self.paginacao.ts_after,
                        self.paginacao.ts_before
                    )
                )
            else:
                query = query.filter(self.model.dt_criacao > self.paginacao.ts_after)
        else:
            query = query.filter(self.model.dt_criacao < self.paginacao.ts_before)
        
        self.paginacao = Paginacao()
        return query