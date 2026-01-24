import pytest

from src.api.auth_api import AuthAPI


@pytest.fixture(scope="session")
def auth_api(base_url, user_credentials):
    return AuthAPI(base_url=base_url)
