from playwright.sync_api import Page

from src.pages.base_page import BasePage


class LoginForm:
    def __init__(self, page: Page):
        self.page = page
        self.login_email_input = self.page.locator('input[data-qa="login-email"]')
        self.login_password_input = self.page.locator('input[data-qa="login-password"]')
        self.login_button = self.page.locator('button[data-qa="login-button"]')

    def login(self, email: str, password: str):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()


class InitialSignUpForm:
    def __init__(self, page: Page):
        self.page = page
        self.signup_name_input = self.page.locator('input[data-qa="signup-name"]')
        self.signup_email_input = self.page.locator('input[data-qa="signup-email"]')
        self.signup_button = self.page.locator('button[data-qa="signup-button"]')

    def signup(self, name: str, email: str):
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()


class AuthPage(BasePage):
    url = "/login"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url=base_url)

        self.login_form = LoginForm(page)
        self.signup_form = InitialSignUpForm(page)

        self.user_label = self.page.locator("i.fa.fa-user + b")
        self.error_message = page.locator("form[action='/login'] p")

    def get_error_text(self):
        return self.error_message.inner_text()
