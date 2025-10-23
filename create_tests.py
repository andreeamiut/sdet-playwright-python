"""Quick script to recreate test files."""

test_smoke_content = '''"""
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
'''

test_regression_content = '''"""
Regression Test Suite
Comprehensive tests for all functionality
"""
import pytest
from pages.automation_page import AutomationPage


@pytest.mark.regression
class TestNavigationLinks:
    """Test navigation link functionality"""

    def test_navigate_to_big_page(self, page):
        """Test navigation to Big Page"""
        automation_page = AutomationPage(page)
        automation_page.navigate()
        
        # Click link and wait for navigation
        automation_page.click_big_page_link()
        page.wait_for_url("**/complicated-page**", timeout=10000)
        
        # Verify URL changed
        assert "complicated-page" in page.url or "big-page" in page.url

    def test_navigate_to_fake_landing_page(self, page):
        """Test navigation to Fake Landing Page"""
        automation_page = AutomationPage(page)
        automation_page.navigate()
        
        # Click link and wait for navigation
        automation_page.click_fake_landing_page_link()
        page.wait_for_url("**/fake-landing-page**", timeout=10000)
        
        # Verify URL changed
        assert "landing" in page.url.lower()

    def test_navigate_to_fake_pricing_page(self, page):
        """Test navigation to Fake Pricing Page"""
        automation_page = AutomationPage(page)
        automation_page.navigate()
        
        # Click link and wait for navigation
        automation_page.click_fake_pricing_page_link()
        page.wait_for_url("**/fake-pricing-page**", timeout=10000)
        
        # Verify URL changed
        assert "pricing" in page.url.lower()


@pytest.mark.regression
class TestPageElements:
    """Test page element visibility and interaction"""

    def test_all_practice_links_visible(self, page):
        """Test that all practice links are visible"""
        automation_page = AutomationPage(page)
        automation_page.navigate()
        
        # Check all main practice links
        assert automation_page.is_visible(automation_page.BIG_PAGE_LINK)
        assert automation_page.is_visible(automation_page.FAKE_LANDING_PAGE_LINK)
        assert automation_page.is_visible(automation_page.FAKE_PRICING_PAGE_LINK)
        assert automation_page.is_visible(automation_page.FILL_FORMS_LINK)

    def test_social_icons_visible(self, page):
        """Test that social media icons are visible"""
        automation_page = AutomationPage(page)
        automation_page.navigate()
        
        # Check at least 3 social icons are present
        social_icons = [
            automation_page.is_visible(automation_page.LINKEDIN_ICON),
            automation_page.is_visible(automation_page.TWITTER_ICON),
            automation_page.is_visible(automation_page.FACEBOOK_ICON),
            automation_page.is_visible(automation_page.INSTAGRAM_ICON),
        ]
        assert sum(social_icons) >= 3

    def test_page_heading_contains_text(self, page):
        """Test that page heading contains expected text"""
        automation_page = AutomationPage(page)
        automation_page.navigate()
        
        heading = automation_page.get_page_heading_text()
        assert "Automation" in heading
        assert "Practice" in heading
'''

# Write the files
with open("tests/test_smoke.py", "w", encoding="utf-8") as f:
    f.write(test_smoke_content)

with open("tests/test_regression.py", "w", encoding="utf-8") as f:
    f.write(test_regression_content)

print("Test files created successfully!")
