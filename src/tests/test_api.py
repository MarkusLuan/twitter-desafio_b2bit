import pytest
import seguranca_utils

class TestApi:
    @pytest.fixture(autouse=True)
    def setup_app_context(self, app_context):
        self.ctx = app_context.app_context()
        self.ctx.push()

        self.tester = app_context.test_client()

        basic_token_user = app_context.config["BASIC_AUTH_USERNAME"]
        basic_token_pass = app_context.config["BASIC_AUTH_PASSWORD"]

        self.URL_AUTH = "/api/auth/token"
        self.basic_token = seguranca_utils.toBase64(f"{basic_token_user}:{basic_token_pass}")
    
    def teardown_method(self):
        self.ctx.pop()
    
    def autenticar (self, usuario: str, senha: str):
        res = self.tester.post(self.URL_AUTH, headers = {
            "Authorization": f"Basic {self.basic_token}"
        }, json={
            "username": usuario,
            "senha": senha
        })

        return res
    
    def test_basic_auth(self):
        res = self.tester.post(self.URL_AUTH)
        j = res.json or {}

        assert res.status_code == 401
    
    def test_oath_token(self):        
        res = self.autenticar("user.teste", seguranca_utils.toBase64("4321"))
        assert res.status_code == 401

        res = self.autenticar("user.teste", seguranca_utils.toBase64("1234"))
        assert res.status_code == 200

    def test_not_found(self):
        res = self.autenticar("user.teste", seguranca_utils.toBase64("1234"))
        j = res.json

        res = self.tester.get("/blabla", headers = {
            "Authorization": f"Bearer {j['access_token']}"
        })

        assert res.status_code == 404
        assert res.is_json is True
        
        j = res.json or {}

        assert j["erro"] is True
        assert j["texto"] == "Recurso não encontrado!"

    def test_not_authorized(self):
        res = self.tester.get("/feed")

        assert res.status_code == 401
        assert res.is_json is True
    
    def test_method_not_allowed(self):
        res = self.autenticar("user.teste", seguranca_utils.toBase64("1234"))
        j = res.json

        res = self.tester.get(self.URL_AUTH, headers = {
            "Authorization": f"Bearer {j['access_token']}"
        })
        
        assert res.status_code in [401, 405]
        assert res.is_json is True