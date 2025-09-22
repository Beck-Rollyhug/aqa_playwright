from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    CHECKOUT_SUMMARY_SELECTOR: str = '[data-test="checkout-summary-container"]'
    CHECKOUT_FINISH_BUTTON_SELECTOR: str = '[data-test="finish"]'

    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint: str = '/checkout-step-two.html'

    def finish_checkout(self):
        self.assert_element_is_visible(self.CHECKOUT_SUMMARY_SELECTOR)
        self.assert_element_is_visible(self.CHECKOUT_FINISH_BUTTON_SELECTOR)
        self.wait_for_selector_and_click(self.CHECKOUT_FINISH_BUTTON_SELECTOR)

