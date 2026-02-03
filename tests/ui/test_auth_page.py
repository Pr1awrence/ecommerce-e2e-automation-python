import pytest
from playwright.sync_api import expect


login_error_message = "Your email or password is incorrect!"


@pytest.mark.ui
def test_login_with_valid_credentials(page, auth_page, home_page, registered_user):
    expected_username = registered_user.name

    home_page.auth_button.click()
    auth_page.login_form.login(registered_user.email, registered_user.password)

    expect(auth_page.user_label).to_be_visible()
    expect(auth_page.user_label).to_have_text(expected_username)


@pytest.mark.ui
def test_login_with_invalid_credentials(page, auth_page, home_page):
    home_page.auth_button.click()
    auth_page.login_form.login("wrong_email@test.com", "wrong_password")
    current_error_text = auth_page.get_error_text()

    assert current_error_text == login_error_message
    expect(page).to_have_url(auth_page.url)
