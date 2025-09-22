from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_SELECTOR: str = '[data-test="username"]'
    PASSWORD_SELECTOR: str = '[data-test="password"]'
    LOGIN_BUTTON_SELECTOR: str = '[data-test="login-button"]'
    INVENTORY_SELECTOR: str = '[data-test="inventory-container"]'

    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint: str = ''

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(self.USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(self.PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.INVENTORY_SELECTOR)
