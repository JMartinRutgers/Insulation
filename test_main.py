from app import app

def app(client):
    response = client.get('/')
    assert b'Static' in response.data

