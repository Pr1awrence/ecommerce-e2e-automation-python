"""
NOTE: This API returns HTTP 200 even for errors.
The real status code is in the 'responseCode' field within the JSON body.
"""

import pytest

from src.models.user_model import fake
from tests.utils import assert_api_response, assert_response_message


@pytest.mark.api
def test_login_with_valid_credentials(auth_api, registered_user):
    response = auth_api.login_user(
        email=registered_user.email, password=registered_user.password
    )

    assert_api_response(response=response, expected_code=200)
    assert_response_message(response=response, expected_message="User exists!")


@pytest.mark.api
def test_login_with_incorrect_email(auth_api):
    response = auth_api.login_user(email=fake.name(), password=fake.password())

    assert_api_response(response=response, expected_code=404)
    assert_response_message(
        response=response,
        expected_message="User not found!",
    )


@pytest.mark.api
def test_login_without_email(auth_api):
    response = auth_api.login_user(password=fake.password())

    assert_api_response(response=response, expected_code=400)
    assert_response_message(
        response=response,
        expected_message="Bad request, email or password parameter is missing in POST request.",
    )


@pytest.mark.api
def test_login_incorrect_password(auth_api, registered_user):
    response = auth_api.login_user(email=registered_user.email, password=fake.password())

    assert_api_response(response=response, expected_code=404)
    assert_response_message(response=response, expected_message="User not found!")


@pytest.mark.api
def test_registration_successful(auth_api, user_data, auto_delete_user):
    auto_delete_user.append(user_data)
    response = auth_api.create_user(user_data)

    assert_api_response(response=response, expected_code=201)
    assert_response_message(response=response, expected_message="User created!")


@pytest.mark.api
def test_registration_existing_email(auth_api, registered_user):
    response = auth_api.create_user(registered_user)

    assert_api_response(response=response, expected_code=400)
    assert_response_message(response=response, expected_message="Email already exists!")


@pytest.mark.api
def test_delete_user_successful(auth_api, user_data):
    auth_api.create_user(user_data)
    response = auth_api.delete_user(user_data.email, user_data.password)

    assert_api_response(response=response, expected_code=200)
    assert_response_message(response=response, expected_message="Account deleted!")


@pytest.mark.api
def test_get_user_details(auth_api, registered_user):
    response = auth_api.get_user(registered_user.email)

    assert_api_response(response=response, expected_code=200)
    assert response.json()["user"]["email"] == registered_user.email
    assert response.json()["user"]["name"] == registered_user.name


@pytest.mark.api
def test_update_user_details(auth_api, registered_user):
    updated_user = registered_user.model_copy()
    new_name = fake.name()

    updated_user.name = new_name

    response = auth_api.update_user(updated_user)

    assert_api_response(response=response, expected_code=200)
    assert_response_message(response=response, expected_message="User updated!")

    response = auth_api.get_user(registered_user.email)
    assert response.json()["user"]["name"] == new_name

    # This API doesn't delete object if name is changed!
    registered_user.name = new_name
