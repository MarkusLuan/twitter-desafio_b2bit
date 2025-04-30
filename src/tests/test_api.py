from app import create_app

def test_not_found():
    app = create_app("config.test")

    tester = app.test_client()
    res = tester.get("/blabla")

    assert res.status_code == 404
    assert res.is_json is True
    
    j = res.json or {}

    assert j["erro"] is True
    assert j["texto"] == "Recurso não encontrado!"