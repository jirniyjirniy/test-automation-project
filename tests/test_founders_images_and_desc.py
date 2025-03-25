from playwright.sync_api import Page, expect


def test_founders_navigation(page: Page):
    """
        Verifies the navigation and content on each founder's profile in the 'Leadership' section of the Bamfunds website.

        Test steps:
        1. Navigate to the Bamfunds homepage.
        2. Hover over the 'About Us' menu item and click on 'Leadership'.
        3. For each founder (Dmitry Balyasny, Taylor O'Malley, and Scott Schroeder):
           - Click on the founder's name to navigate to their profile page.
           - Verify the URL corresponds to the correct founder's profile.
           - Check that the profile page has loaded by waiting for the 'DOMContentLoaded' state.
           - Validate that the founder's name appears in the title.
           - Check that the founder's position is visible and correct.
           - Verify the founder's photo is displayed.
           - Ensure the bio description contains the expected keyword.
           - After verifying the profile, navigate back to the 'Leadership' page.
        4. Navigate through each founder's profile using the 'Next Profile' button to ensure smooth navigation.
        5. Return to the 'Leadership' page after going through all profiles.

        Expected results:
        - Each founder's profile page should load correctly.
        - The title should contain the founder's name.
        - The position, photo, and bio should be correctly displayed and contain the expected information.
        - Navigation through the founder profiles should work with the 'Next Profile' button.
        - After navigation, the user should be returned to the 'Leadership' page.
        """
    page.goto("https://www.bamfunds.com/")
    page.hover("text=About Us")
    page.click("text=Leadership")

    founders = [
        {
            "name": "Dmitry Balyasny",
            "url": "/about-us/leadership/dmitry-balyasny",
            "position": "Managing Partner & Chief Investment Officer",
            "bio_keyword": "co-founded Balyasny Asset Management"
        },
        {
            "name": "Taylor O'Malley",
            "url": "/about-us/leadership/taylor-o-malley",
            "position": "Co-Founding Partner & President",
            "bio_keyword": "Taylor O’Malley is president of"
        },
        {
            "name": "Scott Schroeder",
            "url": "/about-us/leadership/scott-schroeder",
            "position": "Co-Founding Partner",
            "bio_keyword": "Scott Schroeder co-founded Balyasny"
        }
    ]

    for founder in founders:
        page.click(f"text={founder['name']}")
        expect(page).to_have_url(f"https://www.bamfunds.com{founder['url']}")
        page.wait_for_load_state("domcontentloaded")

        header_locator = page.locator("div.font-semibold.text-2xl.lg\\:text-4xl")
        expect(header_locator).to_be_visible()
        assert founder["name"] in header_locator.inner_text().strip(), f"Name {founder['name']} missing in the title"

        position_locator = page.locator("div.font-medium.text-base.leading-7")
        expect(position_locator).to_be_visible()
        assert founder[
                   "position"] in position_locator.inner_text().strip(), f"Expected '{founder['position']}', but we got '{position_locator.inner_text().strip()}'"

        photo_locator = page.locator("img.rounded-full.aspect-square.object-cover")
        expect(photo_locator).to_be_visible()

        description_locator = page.locator("div.font-medium.text-base.leading-relaxed")
        expect(description_locator).to_be_visible()
        assert founder[
                   "bio_keyword"] in description_locator.inner_text(), f"The founder's description {founder['name']} does not contain the expected text"

        page.wait_for_timeout(2000)
        page.go_back()
        expect(page).to_have_url("https://www.bamfunds.com/about-us/leadership")

    page.wait_for_timeout(2000)
    page.click(f"text={founders[0]['name']}")
    expect(page).to_have_url(f"https://www.bamfunds.com{founders[0]['url']}")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1500)

    next_button = page.locator("a[aria-label='Next Profile']")

    for _ in range(len(founders) - 1):
        if next_button.is_visible():
            next_button.click()
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(1500)

    page.goto("https://www.bamfunds.com/about-us/leadership")
    page.wait_for_load_state("domcontentloaded")
    expect(page).to_have_url("https://www.bamfunds.com/about-us/leadership")
