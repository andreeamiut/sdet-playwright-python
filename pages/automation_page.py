"""
Page Object Model for Ultimate QA Automation Page
"""
from pages.base_page import BasePage


class AutomationPage(BasePage):
    """Page Object for Ultimate QA Automation Practice page"""

    # Page URL
    PAGE_URL = "https://ultimateqa.com/automation"

    # Page Elements - Based on actual page structure
    PAGE_TITLE = "h1"
    PAGE_HEADING = "h1:has-text('Automation Practice')"

    # Navigation Links (main content)
    BIG_PAGE_LINK = "a:has-text('Big page with many elements')"
    FAKE_LANDING_PAGE_LINK = "a:has-text('Fake Landing Page')"
    FAKE_PRICING_PAGE_LINK = "a:has-text('Fake Pricing Page')"
    FILL_FORMS_LINK = "a:has-text('Fill out forms')"
    LOGIN_AUTOMATION_LINK = "a:has-text('Login automation')"
    SIMPLE_ELEMENTS_LINK = "a:has-text('Interactions with simple elements')"

    # Social Media Icons
    LINKEDIN_ICON = "a[href*='linkedin']"
    TWITTER_ICON = "a[href*='twitter']"
    FACEBOOK_ICON = "a[href*='facebook']"
    INSTAGRAM_ICON = "a[href*='instagram']"
    YOUTUBE_ICON = "a[href*='youtube']"

    # Navigation Menu
    SERVICES_LINK = "a:has-text('Services')"
    ABOUT_LINK = "a:has-text('About')"
    BLOG_LINK = "a:has-text('Blog')"
    NEWSLETTER_LINK = "a:has-text('Newsletter')"
    EDUCATION_LINK = "a:has-text('Education')"

    def navigate(self, url=None):
        """Navigate to the automation page"""
        target_url = url if url is not None else self.PAGE_URL
        super().navigate(target_url)
        self.verify_page_loaded()

    def verify_page_loaded(self):
        """Verify the page has loaded successfully"""
        self.wait_for_element(self.PAGE_TITLE, state="visible")
        return self.is_visible(self.PAGE_TITLE)

    # Navigation Actions
    def click_big_page_link(self):
        """Click the Big Page link"""
        self.click(self.BIG_PAGE_LINK)

    def click_fake_landing_page_link(self):
        """Click the Fake Landing Page link"""
        self.click(self.FAKE_LANDING_PAGE_LINK)

    def click_fake_pricing_page_link(self):
        """Click the Fake Pricing Page link"""
        self.click(self.FAKE_PRICING_PAGE_LINK)

    # Visibility Checks
    def is_big_page_link_visible(self):
        """Check if Big Page link is visible"""
        return self.is_visible(self.BIG_PAGE_LINK)

    def is_fake_landing_page_link_visible(self):
        """Check if Fake Landing Page link is visible"""
        return self.is_visible(self.FAKE_LANDING_PAGE_LINK)

    def is_twitter_icon_visible(self):
        """Check if Twitter icon is visible"""
        return self.is_visible(self.TWITTER_ICON)

    def is_facebook_icon_visible(self):
        """Check if Facebook icon is visible"""
        return self.is_visible(self.FACEBOOK_ICON)

    def is_linkedin_icon_visible(self):
        """Check if LinkedIn icon is visible"""
        return self.is_visible(self.LINKEDIN_ICON)

    def has_navigation_links(self):
        """Check if navigation links are present"""
        return (
            self.is_visible(self.BIG_PAGE_LINK) and
            self.is_visible(self.FAKE_LANDING_PAGE_LINK) and
            self.is_visible(self.FAKE_PRICING_PAGE_LINK)
        )

    def has_social_media_icons(self):
        """Check if social media icons are present"""
        return (
            self.is_visible(self.LINKEDIN_ICON) or
            self.is_visible(self.TWITTER_ICON) or
            self.is_visible(self.FACEBOOK_ICON)
        )

    def get_page_heading_text(self):
        """Get the main page heading text"""
        return self.get_text(self.PAGE_HEADING)
