import pytest
from playwright.sync_api import Page

from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage


@pytest.fixture
def page(page: Page, base_url) -> Page:
    page.goto(base_url)
    return page


@pytest.fixture
def login_page(page, base_url):
    return LoginPage(page, base_url=base_url)


@pytest.fixture
def home_page(page, base_url):
    return HomePage(page, base_url=base_url)

