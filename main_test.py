# test_hello.py
from main import app


def test_main():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'
    response = app.test_client().get('/cow')
    assert response.status_code == 200
    assert response.data == b'MOoooOo!'
    response = app.test_client().get('/bijnajarig')
    assert response.status_code == 200
    assert response.data == b'almost-b-d!'
