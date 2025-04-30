from app import create_app

import base64

def test_not_found():
    app = create_app("config.test")

    tester = app.test_client()
    res = tester.get("/blabla")

    assert res.status_code == 404
    assert res.is_json is True
    
    j = res.json or {}

    assert j["erro"] is True
    assert j["texto"] == "Recurso não encontrado!"

def test_basic_auth():
    app = create_app("config.test")
    url = "/api/auth/token"

    tester = app.test_client()
    res = tester.get(url)

    assert res.status_code == 405

    res = tester.post(url)
    j = res.json or {}

    assert res.status_code in [400, 500]
    assert j["erro"]
    assert j["texto"] == "'BASIC_AUTH_REALM'"

    basic_token_user = app.config["BASIC_AUTH_USERNAME"]
    basic_token_pass = app.config["BASIC_AUTH_PASSWORD"]
    basic_token = f"{basic_token_user}:{basic_token_pass}".encode("utf-8")
    basic_token = str(base64.b64encode(basic_token), "utf-8")

    res = tester.post(url, headers = {
        "Authorization": f"Basic {basic_token}"
    }, json={
        "user": "teste",
        "password": "1234"
    })
    j = res.json or {}

    assert res.status_code == 200