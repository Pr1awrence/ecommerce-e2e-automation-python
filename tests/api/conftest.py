import json
import os

import pytest

from src.api.auth_api import AuthAPI


@pytest.fixture(scope="session")
def auth_api(base_url, user_credentials):
    return AuthAPI(base_url=base_url)


@pytest.fixture
def new_user_data(user_credentials):
    path = os.path.join(os.path.dirname(__file__), "../../src/test_data/user_data.json")

    with open(path, "r") as f:
        return json.load(f)["new_user"]


@pytest.fixture
def cleanup_registration(auth_api, new_user_data):
    email = new_user_data["email"]
    password = new_user_data["password"]

    auth_api.delete_user(email, password)

    yield

    auth_api.delete_user(email, password)