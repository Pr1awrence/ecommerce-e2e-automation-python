import os

import pytest

from src.api.auth_api import AuthAPI
from src.models.user_model import User


@pytest.fixture(scope="session")
def base_url():
    return os.environ.get("BASE_URL", "")


@pytest.fixture(scope="session")
def auth_api(base_url):
    return AuthAPI(base_url=base_url)


@pytest.fixture
def new_user_data():
    return User()


@pytest.fixture
def registered_user(auth_api, new_user_data, user_cleanup):
    auth_api.create_user(new_user_data)

    return new_user_data


@pytest.fixture
def logged_in_user(auth_api, registered_user):
    auth_api.login_user(email=registered_user.email, password=registered_user.password)

    return registered_user


@pytest.fixture
def user_cleanup(auth_api, new_user_data):
    email = new_user_data.email
    password = new_user_data.password

    auth_api.delete_user(email, password)

    yield

    auth_api.delete_user(email, password)
