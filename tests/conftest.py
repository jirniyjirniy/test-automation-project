import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    import playwright
    playwright.install()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    page.set_viewport_size({"width": 1920, "height": 1080})

    yield page
    page.close()
