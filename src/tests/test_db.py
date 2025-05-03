import pytest
import datetime

from app import create_app
from models import User
from repositories import UsersRepository
from exceptions import user_exceptions
import app_singleton

@pytest.mark.usefixtures("app_context")
class TestUserRepository:
    def setup_method(self):
        self.repository = UsersRepository()

    def test_consulta_vazia(self):
        res = self.repository.search_by_nick_ou_nome("Fulano")
        assert len(res) == 0

    def test_consulta_ok(self):
        res = self.repository.search_by_nick_ou_nome("user.test")
        assert len(res) == 1

    def test_insert(self):
        def cadastrar_usuario():
            self.repository.insert(User(
                dt_nascimento = datetime.date(2000, 1, 26),
                nome = 'Fulano da Silva Sauro',
                nick = 'fulano.risadinha',
                email = 'fulaninho_123@gmail.com',
                senha = '26012000',
                bio = 'e aí bro',
                count_seguidores = 2000,
                count_seguindo = 4
            ))

        
        cadastrar_usuario()
        res = self.repository.search_by_nick_ou_nome("Fulano")
        assert len(res) == 1

        # with pytest.raises(user_exceptions.UserAlreadyRegisteredException):
        #     cadastrar_usuario()