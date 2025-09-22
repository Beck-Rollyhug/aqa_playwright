from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    CHECKOUT_COMPLETE_SELECTOR: str = '[data-test="checkout-complete-container"]'
    HOME_BUTTON_SELECTOR: str = '[data-test="back-to-products"]'
    INVENTORY_SELECTOR: str = '[data-test="inventory-container"]'

    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint: str = '/checkout-step-two.html'

    def back_home(self):
        self.assert_element_is_visible(self.CHECKOUT_COMPLETE_SELECTOR)
        self.wait_for_selector_and_click(self.HOME_BUTTON_SELECTOR)
        self.assert_element_is_visible(self.INVENTORY_SELECTOR)