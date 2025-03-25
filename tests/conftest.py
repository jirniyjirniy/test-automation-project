import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser for tests: chromium, firefox and webkit"
    )


@pytest.fixture(scope="session")
def browser(pytestconfig):
    browser_name = pytestconfig.getoption("--browser")
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=True)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=True)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=True)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    page.set_viewport_size({"width": 1920, "height": 1080})

    yield page
    page.close()
