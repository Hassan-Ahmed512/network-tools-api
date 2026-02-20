from app import app

def test_valid_ip():
    client = app.test_client()
    response = client.get("/check_ip?ip=192.168.1.1")
    assert response.status_code == 200
    assert response.json["valid"] == True

def test_invalid_ip():
    client = app.test_client()
    response = client.get("/check_ip?ip=999.999.999.999")
    assert response.json["valid"] == False
