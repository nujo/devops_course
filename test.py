from app import app

def test_status():
  response = app.test_client().get('/')
  assert response.status_code == 200

def test_contents():
  response = app.test_client().get('/')
  assert b'Myk' in response.data

