from enum import Enum

from playwright.sync_api import Page

from src.pages.base_page import BasePage


class Titles(Enum):
    MR = "Mr"
    MRS = "Mrs"


class SignUpPage(BasePage):
    url = "/signup"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url=base_url)

        self.page_title = page.get_by_role("heading", name="Enter Account Information")
        self.title_radio = lambda value: page.locator(
            f'input[name="title"][value="{value}"]'
        )

    def select_title(self, title: Titles):
        radio = self.title_radio(title)
        radio.check()

    def is_title_selected(self, title: Titles):
        return self.title_radio(title).is_checked()
