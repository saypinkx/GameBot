from server.tests.main import client


def test_create_user(fake_db):
    response = client.post(url='api/users', json={'chat_id': 0, 'parameters': {'test': 'test'}})
    assert response.status_code == 201
    response = client.post(url='api/users', json={'chat_id': 0, 'parameters': {'test': 'test'}})
    assert response.status_code == 400


def test_get_user(fake_db):
    response = client.get(url='api/users/1')
    assert response.status_code == 404
    response = client.get(url='api/users/0')
    assert response.status_code == 200

#
# def test_update_user():
#     response = client.put(url='api/users/0', json={'1': '2'})
#     assert response.status_code == 404
