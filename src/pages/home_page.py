from playwright.sync_api import Page

from src.pages.base_page import BasePage


class HomePage(BasePage):
    url = "/"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url=base_url)
        # Header
        self.signup_login_button = self.page.locator('a[href="/login"]')
