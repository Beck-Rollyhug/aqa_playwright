from playwright.sync_api import Page
from pages.base_page import BasePage


class SidebarPage(BasePage):
    BURGER_MENU_SELECTOR: str = '[id="react-burger-menu-btn"]'
    LOGOUT_LINK_SELECTOR: str = '[data-test="logout-sidebar-link"]'
    LOGIN_FORM_SELECTOR: str = '[data-test="login-container"]'

    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint: str = ''

    def logout(self):
        self.assert_element_is_visible(self.BURGER_MENU_SELECTOR)
        self.wait_for_selector_and_click(self.BURGER_MENU_SELECTOR)
        self.assert_element_is_visible(self.LOGOUT_LINK_SELECTOR)
        self.wait_for_selector_and_click(self.LOGOUT_LINK_SELECTOR)
        self.assert_element_is_visible(self.LOGIN_FORM_SELECTOR)

