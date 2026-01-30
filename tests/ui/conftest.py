import pytest
from playwright.sync_api import Page

from src.pages.home_page import HomePage
from src.pages.auth_page import AuthPage
from src.pages.signup_page import SignUpPage


@pytest.fixture
def page(page: Page, base_url) -> Page:
    page.goto(base_url)
    return page


@pytest.fixture
def auth_page(page, base_url):
    return AuthPage(page, base_url=base_url)


@pytest.fixture
def home_page(page, base_url):
    return HomePage(page, base_url=base_url)


@pytest.fixture
def signup_page(page, base_url):
    return SignUpPage(page, base_url=base_url)
