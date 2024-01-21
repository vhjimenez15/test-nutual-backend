import pytest
from app import app as app_


@pytest.fixture()
def client():
    with app_.test_client() as client:
        yield client
