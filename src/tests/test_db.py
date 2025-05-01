import datetime

from app import create_app
from models import User
from repositories import UsersRepository
import app_singleton

class TestUserRepository:
    @classmethod
    def setup_class(cls):
        app = create_app("config.test")
        
        cls.app_context = app.app_context()
        cls.app_context.push()
        app_singleton.db.create_all()

        cls.repository = UsersRepository()

    def test_consulta_vazia(self):
        res = self.repository.search_by_nick_ou_nome("Fulano")
        assert len(res) == 0

    def test_insert(self):
        self.repository.insert(User(**{
            "id": 0,
            "dt_nascimento": datetime.date(2000, 1, 26),
            "nome": 'Fulano da Silva Sauro',
            "nick": 'fulano.risadinha',
            "email": 'fulaninho_123@gmail.com',
            "senha": '26012000',
            "bio": 'e aí bro',
            "count_seguidores": 2000,
            "count_seguindo": 4
        }))

        res = self.repository.search_by_nick_ou_nome("Fulano")
        assert len(res) == 1