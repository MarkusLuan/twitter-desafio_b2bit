from app import app

def test_not_found():
    tester = app.test_client()
    res = tester.get("/blabla")

    assert res.status_code == 404
    assert res.is_json is True
    
    j = res.json or {}

    assert j["erro"] is True
    assert j["texto"] == "Recurso não encontrado!"