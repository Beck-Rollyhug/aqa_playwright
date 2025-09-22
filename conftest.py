import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    yield browser
    browser.close()
    playwright.stop()
