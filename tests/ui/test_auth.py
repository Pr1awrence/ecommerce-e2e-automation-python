import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_login_with_valid_credentials(login_page, user_credentials):
    expected_username = "test"

    login_page.login(user_credentials["email"], user_credentials["password"])

    expect(login_page.user_label).to_be_visible()
    expect(login_page.user_label).to_have_text(expected_username)
