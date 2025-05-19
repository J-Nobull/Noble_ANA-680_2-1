import pytest
from app680_21 import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    # Optionally check content:
    # assert b"expected text" in response.data
if __name__ == "__main__":
    pytest.main()
# Add more tests for your other routes below
