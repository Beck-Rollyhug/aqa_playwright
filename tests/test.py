import allure
import pytest

from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage

BASE_URL = 'https://www.saucedemo.com/'


@pytest.mark.production
def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_complete_page = CheckoutCompletePage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('jhon', 'snow', '12345')
    checkout_page.continue_checkout()
    checkout_overview_page.finish_checkout()
    checkout_complete_page.back_home()


@pytest.mark.production
def test_logout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.login('standard_user', 'secret_sauce')
    sidebar_page = SidebarPage(page)
    sidebar_page.logout()
