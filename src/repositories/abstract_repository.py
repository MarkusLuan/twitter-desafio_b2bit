from sqlalchemy import between
from sqlalchemy.orm import Query

from abc import ABC, abstractmethod
import uuid

from models import Paginacao
import app_singleton

class AbstractRepository (ABC):
    paginacao = Paginacao()

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
                        "dt_criacao",
                        self.paginacao.ts_after,
                        self.paginacao.ts_before
                    )
                )
            else:
                # TODO: Implementar paginação para after
                # query = query.filter("dt_criacao > paginacao.ts_after")
                ...
        else:
            # TODO: Implementar paginação para before
            # query = query.filter("dt_criacao < paginacao.ts_before")
            ...
        
        self.paginacao = Paginacao()
        return query