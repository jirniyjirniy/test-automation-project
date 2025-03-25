from playwright.sync_api import Page


def test_contact_form_validation(page: Page):
    """
        Verifies the contact form validation on the 'Contact Us' page of the Bamfunds website.

        Test steps:
        1. Navigate to the homepage of the Bamfunds website.
        2. Scroll to the footer and click the 'Contact Us' link to navigate to the contact form page.
        3. Attempt to submit the form without filling in any fields.
        4. Check for the appearance of error messages for required fields:
           - "First Name is required"
           - "Last Name is required"
           - "Email Address is required"
           - "Message is required"
        5. Fill in the form with invalid email (test@invalid).
        6. Attempt to submit the form with the invalid email and check for an error message:
           - "There was an error submitting the form. Please try again or refresh the page."

        Expected results:
        1. Error messages for all required fields should be visible when attempting to submit the form without data.
        2. After submitting the form with an invalid email, an error message should appear indicating the form submission failed.
        """
    page.goto("https://www.bamfunds.com/")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.locator('footer a[href="/contact-us"]').nth(1).click()

    page.click('button[type="submit"]')

    assert page.locator(
        'p.text-red-600:has-text("This field is required") >> nth=0').is_visible(), "First Name error not visible"
    assert page.locator(
        'p.text-red-600:has-text("This field is required") >> nth=1').is_visible(), "Last Name error not visible"
    assert page.locator(
        'p.text-red-600:has-text("This field is required") >> nth=2').is_visible(), "Email Address error not visible"
    assert page.locator(
        'p.text-red-600:has-text("This field is required") >> nth=3').is_visible(), "Message error not visible"

    page.locator('input[name="first_name"]').type("John", delay=100)
    page.locator('input[name="last_name"]').type("Doe", delay=100)
    page.locator('input[name="email_address"]').type("test@invalid", delay=100)
    page.locator('textarea[name="message"]').type("This is a test message.", delay=50)

    page.wait_for_timeout(1000)

    page.click('button[type="submit"]')

    error_message_locator = page.locator(
        'div[role="alert"] >> text="There was an error submitting the form. Please try again or refresh the page."'
    )
    error_message_locator.wait_for(state="visible")

    assert error_message_locator.is_visible(), "Error message after invalid email not visible"
