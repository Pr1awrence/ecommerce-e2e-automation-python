import os

import pytest


@pytest.fixture(scope="session")
def base_url():
    return os.environ.get("BASE_URL", "")


@pytest.fixture(scope="session")
def user_credentials():
    return {
        "email": os.environ.get("USER_EMAIL", ""),
        "password": os.environ.get("USER_PASSWORD", ""),
    }
