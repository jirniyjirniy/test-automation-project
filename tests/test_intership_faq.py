import time
from playwright.sync_api import Page, expect


def test_internship_faq(page: Page):
    """
        Verifies the functionality of the FAQ section on the Internship page of the Bamfunds website.

        Test steps:
        1. Navigate to the Bamfunds homepage.
        2. Hover over the 'Careers' menu item and click on the 'Internship' link.
        3. Wait for the FAQ section to load and scroll it into view.
        4. For each FAQ question:
           - Scroll the question into view.
           - Click on the question to reveal the answer.
           - Wait for the answer to appear.
           - Verify that the answer is visible for each question.

        Expected results:
        - Each FAQ question should display an answer when clicked.
        - The answer should be visible and correctly associated with the question.
        """
    page.goto("https://www.bamfunds.com/")
    page.hover("text=Careers")
    page.click("text=Internship")
    page.wait_for_timeout(2000)

    faq_header = page.locator("p:has-text('FAQ')")
    faq_header.scroll_into_view_if_needed()
    page.wait_for_timeout(2000)

    faq_items = page.locator("dl div button")

    for i in range(faq_items.count()):
        question = faq_items.nth(i)
        question.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        question.click()
        page.wait_for_timeout(1500)

        answer = question.locator("xpath=ancestor::dt/following-sibling::dd/div")
        answer.wait_for(state="visible", timeout=3000)

        assert answer.count() > 0, f"Ответ для вопроса '{question.inner_text()}' не найден"

    time.sleep(5)
