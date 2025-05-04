import pytest
import datetime

from app import create_app
from models import User
from repositories import UsersRepository
import seguranca_utils
import app_singleton

@pytest.fixture(scope="session")
def app_context():
    app = create_app("config.test")
    ctx = app.app_context()
    ctx.push()
    app_singleton.db.create_all()

    users_repository = UsersRepository()

    # Garantindo que tenha um usuario no banco de teste
    users_repository.insert(User(
        dt_nascimento = datetime.date.today(),
        nome = 'Usuário de Teste',
        nick = 'user.teste',
        email = 'teste@mail.com',
        senha = seguranca_utils.toBase64('1234'),
        bio = 'testando'
    ))
    app_singleton.db.session.commit()

    yield app

    app_singleton.db.session.remove()
    app_singleton.db.drop_all()
    ctx.pop()