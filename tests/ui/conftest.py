import pytest
from playwright.sync_api import Page

from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage


@pytest.fixture(scope="function")
def page(page: Page, base_url) -> Page:
    page.goto(base_url)
    return page


@pytest.fixture(scope="function")
def login_page(page, base_url):
    return LoginPage(page, base_url=base_url)


@pytest.fixture(scope="function")
def home_page(page, base_url):
    return HomePage(page, base_url=base_url)


@pytest.fixture(scope="function")
def user_is_logged_in(login_page, user_credentials):
    login_page.login(
        email=user_credentials["email"], password=user_credentials["password"]
    )
