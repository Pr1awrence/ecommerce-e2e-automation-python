import calendar

from playwright.sync_api import Page

from src.models.user_model import User
from src.pages.base_page import BasePage


class SignUpPage(BasePage):
    url = "/signup"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url=base_url)

        self.page_title = page.get_by_role("heading", name="Enter Account Information")
        self.gender_mr = page.locator("#id_gender1")
        self.gender_mrs = page.locator("#id_gender2")
        self.password_input = page.get_by_label("Password")

        self.days_select = page.locator("#days")
        self.months_select = page.locator("#months")
        self.years_select = page.locator("#years")

        self.first_name_input = page.locator("#first_name")
        self.last_name_input = page.locator("#last_name")
        self.address_input = page.locator("#address1")
        self.country_select = page.locator("#country")
        self.state_input = page.locator("#state")
        self.city_input = page.locator("#city")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_input = page.locator("#mobile_number")

        self.create_account_btn = page.get_by_role("button", name="Create Account")

    def select_title(self, title: str):
        self.gender_mr.check() if title == "Mr" else self.gender_mrs.check()

    def fill_account_detail_form(self, user: User):
        self.select_title(user.title)

        self.password_input.fill(user.password)

        self.days_select.select_option(str(user.birth_date))

        month_name = calendar.month_name[user.birth_month]
        self.months_select.select_option(label=month_name)

        self.years_select.select_option(str(user.birth_year))

        self.first_name_input.fill(user.firstname)
        self.last_name_input.fill(user.lastname)
        self.address_input.fill(user.address1)
        self.country_select.select_option(user.country)
        self.state_input.fill(user.state)
        self.city_input.fill(user.city)
        self.zipcode_input.fill(user.zipcode)
        self.mobile_input.fill(user.mobile_number)

    def submit_form(self):
        self.create_account_btn.click()
