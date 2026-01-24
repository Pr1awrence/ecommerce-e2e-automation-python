from playwright.sync_api import Page


class BasePage:
    url = ""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def navigate_to(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str):
        self.page.locator(selector).fill(value)

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content()
