import pytest


@pytest.mark.api
def test_login_api_with_valid_credentials(auth_api, registered_user):
    response = auth_api.login_user(
        email=registered_user["email"], password=registered_user["password"]
    )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "User exists!"


@pytest.mark.api
def test_login_api_without_email(auth_api):
    response = auth_api.login_user(
        password="something"
    )

    # This API returns HTTP 200 even for errors.
    # The real status code is provided in the 'responseCode' field within the JSON body.
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["responseCode"] == 400
    assert response_data["message"] == "Bad request, email or password parameter is missing in POST request."


@pytest.mark.api
def test_login_api_incorrect_password(auth_api, registered_user):
    response = auth_api.login_user(
        email=registered_user["email"], password="123"
    )

    # This API returns HTTP 200 even for errors.
    # The real status code is provided in the 'responseCode' field within the JSON body.
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["responseCode"] == 404
    assert response_data["message"] == "User not found!"


@pytest.mark.api
def test_registration_api_successful(auth_api, new_user_data, user_cleanup):
    response = auth_api.create_user(new_user_data)

    assert response.status_code == 200
    assert response.json()["responseCode"] == 201
    assert response.json()["message"] == "User created!"