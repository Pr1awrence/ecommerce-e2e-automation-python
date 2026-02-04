import pytest
from playwright.sync_api import expect


EXPECTED_ERROR_TEXT = "Your email or password is incorrect!"


@pytest.mark.ui
def test_login_with_valid_credentials(page, auth_page, home_page, registered_user):
    expected_username = registered_user.name

    home_page.auth_button.click()
    auth_page.login_form.login(registered_user.email, registered_user.password)

    expect(auth_page.user_label).to_be_visible()
    expect(auth_page.user_label).to_have_text(expected_username)


@pytest.mark.ui
def test_login_with_invalid_credentials(page, auth_page, home_page):
    page.route("**/api/verifyLogin", lambda route: route.fulfill(
        status=200,
        body='{"responseCode": 404, "message": "Your email or password is incorrect!"}'
    ))

    home_page.auth_button.click()
    auth_page.login_form.login("test@mock.com", "123456")

    expect(auth_page.error_message).to_have_text(EXPECTED_ERROR_TEXT)
    expect(page).to_have_url(auth_page.url)
