import pytest
import datetime

from app import create_app
from models import User
import app_singleton

@pytest.fixture(scope="session")
def app_context():
    app = create_app("config.test")
    ctx = app.app_context()
    ctx.push()
    app_singleton.db.create_all()

    # Garantindo que tenha um usuario no banco de teste
    app_singleton.db.session.add(User(
        dt_nascimento = datetime.date.today(),
        nome = 'Usuário de Teste',
        nick = 'user.teste',
        email = 'teste@mail.com',
        senha = '1234',
        bio = 'testando'
    ))
    app_singleton.db.session.commit()

    yield app

    app_singleton.db.session.remove()
    app_singleton.db.drop_all()
    ctx.pop()