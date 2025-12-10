from http.client import responses

import requests


def test_get_user():
    url = "https://reqres.in/api/users/2"  # Free mock API
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2
    assert "janet.weaver@reqres.in" in response.json()["data"]["email"]


def test_create_user():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "John Doe",
        "job": "Software Engineer"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_update_user():
    url = "https://reqres.in/api/users/2"
    payload = {
        "name": "Updated Name",
        "job": "Senior QA"
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    assert response.json()["job"] == "Senior QA"

def test_delete_user():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url)

    assert response.status_code == 204

def test_jwt_auth_sucsess():
    url = "https://reqres.in/api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response  = requests.post(url, json=payload)
    assert response.status_code == 200
    assert "token" in response.json()