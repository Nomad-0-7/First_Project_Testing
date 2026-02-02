import pytest
from api_client import APIClient

client = APIClient()

# Test Data
REGISTER_DATA = {"username":"Dummy", "email":"Dummy@gmail.com", "Password":"Dummy123"}
LOGIN_DATA = {"email":"Dummy@gmail.com", "Password":"Dummy123"}

def test_user_registration():
    response = client.post("/api/User_Authentication/Register", REGISTER_DATA)
    assert response.status_code == 200
    # You can add more specific assertions here
    assert "success" in response.text.lower()

def test_user_login():
    response = client.post("/api/User_Authentication/Login", LOGIN_DATA)
    assert response.status_code == 200