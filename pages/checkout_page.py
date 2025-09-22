from playwright.sync_api import Page
from pages.base_page import BasePage

WITH_DELAY: int = 100


class CheckoutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR: str = '[data-test="checkout"]'
    FIRST_NAME_SELECTOR: str = '[data-test="firstName"]'
    LAST_NAME_SELECTOR: str = '[data-test="lastName"]'
    POSTAL_CODE_SELECTOR: str = '[data-test="postalCode"]'
    CONTINUE_SELECTOR: str = '[data-test="continue"]'
    CHECKOUT_SUMMARY_SELECTOR: str = '[data-test="checkout-summary-container"]'

    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint: str = '/checkout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.FIRST_NAME_SELECTOR)

    def fill_checkout_form(self, firstname, lastname, postal_code):
        self.wait_for_selector_and_type(
            self.FIRST_NAME_SELECTOR, firstname, WITH_DELAY)
        self.wait_for_selector_and_type(
            self.LAST_NAME_SELECTOR, lastname, WITH_DELAY)
        self.wait_for_selector_and_type(
            self.POSTAL_CODE_SELECTOR, postal_code, WITH_DELAY)
        self.assert_input_value(self.POSTAL_CODE_SELECTOR, postal_code)

    def continue_checkout(self):
        self.wait_for_selector_and_click(self.CONTINUE_SELECTOR)
        self.assert_element_is_visible(self.CHECKOUT_SUMMARY_SELECTOR)
