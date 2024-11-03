from fastapi.testclient import TestClient

from brilliant_api.main import app


client = TestClient(app)

def test_add_brilliant_thing():
    response = client.post('/brilliant_thing', json={"entry": "rainy days"})
    assert response.status_code == 201

def test_get_brilliant_thing():
    response = client.get('/brilliant_thing')
    assert response.status_code == 200
