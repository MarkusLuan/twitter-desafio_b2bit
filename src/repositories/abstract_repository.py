from abc import ABC, abstractmethod
import uuid

import app_singleton

class AbstractRepository (ABC):
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