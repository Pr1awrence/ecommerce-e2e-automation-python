def assert_api_response(response, expected_code):
    assert response.status_code == 200, (
        f"Unexpected HTTP status: {response.status_code}"
    )

    data = response.json()
    current_code = data.get("responseCode")

    assert current_code == expected_code, (
        f"Test failure / Status code: Expected {expected_code} responseCode, but got {current_code}. Full response: {data}"
    )


def assert_response_message(response, expected_message):
    data = response.json()
    current_message = data["message"]

    assert current_message == expected_message, (
        f"Test failure / Response message: Expected {expected_message} message, but got {current_message}. Full response: {data}"
    )
