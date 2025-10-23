"""
Smoke Test Suite
Quick tests to verify basic functionality
"""
import pytest
from pages.automation_page import AutomationPage


@pytest.mark.smoke
@pytest.mark.critical
class TestBasicFunctionality:
    """Basic smoke tests for critical functionality"""

    def test_page_loads_successfully(self, page):
        """Test that the automation page loads successfully"""
        automation_page = AutomationPage(page)
        automation_page.navigate()
        assert automation_page.verify_page_loaded()
        assert "automation" in page.url.lower()

    def test_page_has_essential_elements(self, page):
        """Test that essential page elements are present"""
        automation_page = AutomationPage(page)
        automation_page.navigate()
        assert automation_page.has_navigation_links()
        assert automation_page.has_social_media_icons()

    def test_navigation_links_are_visible(self, page):
        """Test that navigation links are visible"""
        automation_page = AutomationPage(page)
        automation_page.navigate()
        assert automation_page.is_big_page_link_visible()
        assert automation_page.is_fake_landing_page_link_visible()

    def test_social_media_icons_present(self, page):
        """Test that social media icons are present"""
        automation_page = AutomationPage(page)
        automation_page.navigate()
        assert (
            automation_page.is_twitter_icon_visible() or
            automation_page.is_facebook_icon_visible() or
            automation_page.is_linkedin_icon_visible()
        )
