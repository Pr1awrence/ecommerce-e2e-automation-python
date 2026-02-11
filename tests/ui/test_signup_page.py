import pytest

pytestmark = pytest.mark.ui

from playwright.sync_api import expect


@pytest.mark.smoke
def test_initial_signup_submit(page, home_page, auth_page, signup_page, user_data):
    home_page.auth_button.click()
    auth_page.signup_form.signup_name_input.fill(user_data.name)
    auth_page.signup_form.signup_email_input.fill(user_data.email)
    auth_page.signup_form.signup_button.click()

    expect(page).to_have_url(signup_page.url)


@pytest.mark.smoke
def test_signup_user_successful(
    page,
    home_page,
    auth_page,
    signup_page,
    account_created_page,
    user_data,
    auto_delete_user,
):
    auto_delete_user.append(user_data)

    home_page.auth_button.click()
    auth_page.signup_form.signup(name=user_data.name, email=user_data.email)
    signup_page.fill_account_detail_form(user_data)
    signup_page.submit_form()

    expect(account_created_page.page_title).to_be_visible()
    expect(page).to_have_url(account_created_page.url)
