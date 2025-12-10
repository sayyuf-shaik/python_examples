import pytest

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def user_data():
    return {"name": "John", "job": "Engineer"}