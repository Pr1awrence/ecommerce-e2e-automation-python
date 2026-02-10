import pytest

pytestmark = pytest.mark.ui

from playwright.sync_api import expect

from src.models.user_model import fake

INCORRECT_EMAIL_OR_PASSWORD_ERROR_TEXT = "Your email or password is incorrect!"
EMAIL_EXISTS_ERROR_TEXT = "Email Address already exist!"

BUG_16_URL_CHANGE = (
    "https://github.com/Pr1awrence/ecommerce-e2e-automation-python/issues/16"
)


def test_login_with_valid_credentials(auth_page, home_page, registered_user):
    expected_username = registered_user.name

    home_page.auth_button.click()
    auth_page.login_form.login(registered_user.email, registered_user.password)

    expect(auth_page.user_label).to_be_visible(timeout=10000)
    expect(auth_page.user_label).to_have_text(expected_username)


def test_login_with_invalid_credentials(page, auth_page, home_page):
    page.route(
        "**/api/verifyLogin",
        lambda route: route.fulfill(
            status=200,
            body='{"responseCode": 404, "message": "Your email or password is incorrect!"}',
        ),
    )

    home_page.auth_button.click()
    auth_page.login_form.login(fake.email(), fake.password())

    expect(auth_page.login_form.error_message).to_have_text(
        INCORRECT_EMAIL_OR_PASSWORD_ERROR_TEXT
    )
    expect(page).to_have_url(auth_page.url)


def test_login_with_invalid_password(page, auth_page, home_page, registered_user):
    page.route(
        "**/api/verifyLogin",
        lambda route: route.fulfill(
            status=200,
            body='{"responseCode": 404, "message": "Your email or password is incorrect!"}',
        ),
    )

    home_page.auth_button.click()
    auth_page.login_form.login(registered_user.email, fake.password())

    expect(auth_page.login_form.error_message).to_have_text(
        INCORRECT_EMAIL_OR_PASSWORD_ERROR_TEXT
    )
    expect(page).to_have_url(auth_page.url)


def test_initial_signup_successful(page, auth_page, signup_page, home_page):
    page.route(
        "**/api/signup",
        lambda route: route.fulfill(
            status=200, body='{"responseCode": 200, "message": "smth"}'
        ),
    )

    home_page.auth_button.click()
    auth_page.signup_form.signup(fake.name(), fake.email())

    expect(signup_page.page_title).to_be_visible()
    expect(page).to_have_url(signup_page.url)


@pytest.mark.xfail(reason=f"Bug: URL changes incorrectly. See {BUG_16_URL_CHANGE}")
def test_initial_signup_existing_email(page, auth_page, home_page, registered_user):
    page.route(
        "**/api/signup",
        lambda route: route.fulfill(
            status=200,
            body='{"responseCode": 404, "message": "Your email or password is incorrect!"}',
        ),
    )

    home_page.auth_button.click()
    auth_page.signup_form.signup(registered_user.name, registered_user.email)

    expect(auth_page.signup_form.error_message).to_have_text(EMAIL_EXISTS_ERROR_TEXT)
    expect(page).to_have_url(auth_page.url)
