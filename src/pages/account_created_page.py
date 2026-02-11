from playwright.sync_api import Page

from src.pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    url = "/account_created"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url=base_url)

        self.page_title = page.get_by_role("heading", name="Account Created!")
        self.continue_button = page.locator("#continue-button")

    def continue_button_click(self):
        self.continue_button.click()
