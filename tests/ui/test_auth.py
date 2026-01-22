import pytest
from playwright.sync_api import expect


login_error_message = "Your email or password is incorrect!"


@pytest.mark.smoke
def test_login_with_valid_credentials(page, login_page, home_page, user_credentials):
    expected_username = "test"

    home_page.signup_login_button.click()
    login_page.login(user_credentials["email"], user_credentials["password"])

    expect(login_page.user_label).to_be_visible()
    expect(login_page.user_label).to_have_text(expected_username)


@pytest.mark.regression
def test_login_with_invalid_credentials(page, login_page, home_page, user_credentials):
    home_page.signup_login_button.click()
    login_page.login("wrong_email@test.com", "wrong_password")
    current_error_text = login_page.get_error_text()

    assert current_error_text == login_error_message
    expect(page).to_have_url(login_page.url)
