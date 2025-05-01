import datetime

from app import create_app
from models import User
from repositories import UsersRepository
import app_singleton

def test_insert_user():
    app = create_app("config.test")
    with app.app_context():
        app_singleton.db.create_all()

        repository = UsersRepository()
        res = repository.search_by_nick_ou_nome("Fulano")

        assert len(res) == 0

        repository.insert(User(**{
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

        res = repository.search_by_nick_ou_nome("Fulano")
        assert len(res) == 1