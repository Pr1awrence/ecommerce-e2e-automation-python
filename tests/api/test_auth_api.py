import pytest


@pytest.mark.api
def test_login_api_with_valid_credentials(auth_api, user_credentials):
    response = auth_api.login_user(
        email=user_credentials["email"], password=user_credentials["password"]
    )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "User exists!"
