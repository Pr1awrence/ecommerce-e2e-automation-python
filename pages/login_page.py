from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_email_input = self.page.locator('input[data-qa="login-email"]')
        self.login_password_input = self.page.locator('input[data-qa="login-password"]')
        self.login_button = self.page.locator('button[data-qa="login-button"]')
        self.user_label = self.page.locator("i.fa.fa-user + b")

    def login(self, email: str, password: str):
        self.page.goto("https://automationexercise.com/login")
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()
