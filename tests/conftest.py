import logging
import os

import pytest

from src.api.auth_client import AuthClient


@pytest.fixture(scope="session")
def base_url():
    return os.environ.get("BASE_URL", "")


@pytest.fixture(scope="session")
def auth_api(base_url):
    return AuthClient(base_url=base_url)


@pytest.fixture
def user_factory():
    from src.models.user_model import User

    return User


@pytest.fixture
def user_data(user_factory):
    return user_factory()


@pytest.fixture
def auto_delete_user(auth_api):
    users_to_delete = []

    yield users_to_delete

    for user in users_to_delete:
        try:
            auth_api.delete_user(user.email, user.password)
        except Exception as e:
            logging.error(f"Failed to delete user {user.email}: {e}")


@pytest.fixture
def registered_user(auth_api, user_data, auto_delete_user):
    auth_api.create_user(user_data)
    auto_delete_user.append(user_data)
    return user_data


@pytest.fixture
def logged_in_user(auth_api, registered_user):
    auth_api.login_user(email=registered_user.email, password=registered_user.password)

    return registered_user
