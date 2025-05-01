import base64
import datetime

from app import create_app
from models import User
from repositories import UsersRepository
import app_singleton

app = create_app("config.test")

class TestApi:
    @classmethod
    def setup_class(cls):
        cls.tester = app.test_client()

        cls.app_context = app.app_context()
        cls.app_context.push()
        app_singleton.db.create_all()

        cls.URL_AUTH = "/api/auth/token"

    def test_not_found(self):
        res = self.tester.get("/blabla")

        assert res.status_code == 404
        assert res.is_json is True
        
        j = res.json or {}

        assert j["erro"] is True
        assert j["texto"] == "Recurso não encontrado!"
    
    def test_method_not_allowed(self):
        res = self.tester.get(self.URL_AUTH)
        
        assert res.status_code == 405
        assert res.is_json is True
        
        j = res.json or {}
        assert j["erro"] is True

    def test_basic_auth(self):
        res = self.tester.post(self.URL_AUTH)
        j = res.json or {}

        assert res.status_code == 401
    
    def test_oath_token(self):
        def autenticar ():
            basic_token_user = app.config["BASIC_AUTH_USERNAME"]
            basic_token_pass = app.config["BASIC_AUTH_PASSWORD"]
            basic_token = f"{basic_token_user}:{basic_token_pass}".encode("utf-8")
            basic_token = str(base64.b64encode(basic_token), "utf-8")

            res = self.tester.post(self.URL_AUTH, headers = {
                "Authorization": f"Basic {basic_token}"
            }, json={
                "username": "user.teste",
                "senha": "1234"
            })

            return res
        
        res = autenticar()
        assert res.status_code == 401

        UsersRepository().insert(User(**{
            "id": 0,
            "dt_nascimento": datetime.date.today(),
            "nome": 'Usuário de Teste',
            "nick": 'user.teste',
            "email": 'teste@mail.com',
            "senha": '1234',
            "bio": 'testando'
        }))

        res = autenticar()
        assert res.status_code == 200