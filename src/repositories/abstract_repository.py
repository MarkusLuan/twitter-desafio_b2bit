from abc import ABC, abstractmethod
import uuid

import app_singleton

class AbstractRepository (ABC):
    @abstractmethod
    def get_by_uuid(self, _uuid: uuid.UUID):
        ...
    
    def insert(self, _entity):
        app_singleton.db.session.add(_entity)
        app_singleton.db.session.commit()

        return _entity