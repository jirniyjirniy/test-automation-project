from playwright.sync_api import Page, expect


def test_founders_section(page: Page):
    """
        Verifies the visibility of the founders' names in the 'Leadership' section on the Bamfunds website.

        Test steps:
        1. Navigate to the Bamfunds homepage.
        2. Hover over the 'About Us' menu item and click on 'Leadership'.
        3. Iterate through the list of founders' names:
           - Dmitry Balyasny
           - Taylor O'Malley
           - Scott Schroeder
        4. For each founder:
           - Locate the founder's name on the page.
           - Scroll the element into view if needed.
           - Hover over the founder's name.
           - Ensure that the founder's name is visible on the page.

        Expected result:
        - Each founder's name should be visible after hovering over it.
        """
    page.goto("https://www.bamfunds.com/")

    page.hover("text=About Us")
    page.click("text=Leadership")

    founders = ["Dmitry Balyasny", "Taylor O'Malley", "Scott Schroeder"]

    for founder in founders:
        founder_element = page.locator(f"text={founder}")

        founder_element.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        founder_element.hover()
        page.wait_for_timeout(500)

        expect(founder_element).to_be_visible()
