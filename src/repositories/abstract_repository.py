from abc import ABC, abstractmethod
import uuid

class AbstractRepository (ABC):
    @abstractmethod
    def get_by_uuid(self, _uuid: uuid.UUID):
        ...
    
    @abstractmethod
    def insert(self, _entity):
        ...