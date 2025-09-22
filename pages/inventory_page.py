from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_SELECTOR: str = ".inventory_item >> text='Add to cart'"
    SHOPPING_CART_LINK_SELECTOR: str = '[data-test="shopping-cart-link"]'
    SHOPPING_CART_BADGE_SELECTOR: str = '[data-test="shopping-cart-badge"]'

    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint: str = '/inventory.html'

    def add_first_item_to_cart(self):
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        self.wait_for_selector_and_click(self.ADD_TO_CART_SELECTOR)
        self.assert_element_is_visible(self.SHOPPING_CART_BADGE_SELECTOR)
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)


