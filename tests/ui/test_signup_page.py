import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.ui
def test_initial_signup_submit(page, auth_page, home_page, signup_page, user_data):
    home_page.auth_button.click()
    auth_page.signup_form.signup_name_input.fill(user_data.name)
    auth_page.signup_form.signup_email_input.fill(user_data.email)
    auth_page.signup_form.signup_button.click()

    expect(page).to_have_url(signup_page.url)
