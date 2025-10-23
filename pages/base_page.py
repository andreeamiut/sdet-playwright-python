"""
Base Page Object Model
Contains common methods used across all page objects
"""
from typing import Optional, List
from playwright.sync_api import Page, Locator, expect, Error
from utils.logger import get_logger


class BasePage:
    """Base Page Object containing common functionality for all pages"""

    def __init__(self, page: Page, timeout: int = 30000):
        """
        Initialize base page

        Args:
            page: Playwright Page object
            timeout: Default timeout in milliseconds
        """
        self.page = page
        self.timeout = timeout
        self.logger = get_logger(self.__class__.__name__)

    def _get_element(self, locator: str | Locator) -> Locator:
        """
        Get element locator

        Args:
            locator: Element locator (string or Locator object)

        Returns:
            Locator object
        """
        if isinstance(locator, str):
            return self.page.locator(locator)
        return locator

    def navigate(self, url: str) -> None:
        """
        Navigate to a specific URL

        Args:
            url: URL to navigate to
        """
        self.logger.info("Navigating to: %s", url)
        self.page.goto(url, timeout=self.timeout, wait_until="domcontentloaded")

    def get_title(self) -> str:
        """
        Get page title

        Returns:
            Page title as string
        """
        title = self.page.title()
        self.logger.debug("Page title: %s", title)
        return title

    def get_url(self) -> str:
        """
        Get current page URL

        Returns:
            Current URL as string
        """
        url = self.page.url
        self.logger.debug("Current URL: %s", url)
        return url

    def click(self, locator: str | Locator, timeout: Optional[int] = None) -> None:
        """
        Click on an element

        Args:
            locator: Element locator (string or Locator object)
            timeout: Custom timeout in milliseconds
        """
        timeout = timeout or self.timeout
        element = self._get_element(locator)
        self.logger.info("Clicking element: %s", locator)
        element.click(timeout=timeout)

    def double_click(self, locator: str | Locator) -> None:
        """
        Double click on an element

        Args:
            locator: Element locator
        """
        element = self._get_element(locator)
        self.logger.info("Double clicking element: %s", locator)
        element.dblclick()

    def fill(self, locator: str | Locator, text: str, timeout: Optional[int] = None) -> None:
        """
        Fill text in an input field

        Args:
            locator: Element locator
            text: Text to fill
            timeout: Custom timeout in milliseconds
        """
        timeout = timeout or self.timeout
        element = self._get_element(locator)
        self.logger.info("Filling text '%s' in element: %s", text, locator)
        element.fill(text, timeout=timeout)

    def type_text(self, locator: str | Locator, text: str, delay: int = 50) -> None:
        """
        Type text character by character

        Args:
            locator: Element locator
            text: Text to type
            delay: Delay between keystrokes in milliseconds
        """
        element = self._get_element(locator)
        self.logger.info("Typing text '%s' in element: %s", text, locator)
        element.type(text, delay=delay)

    def clear(self, locator: str | Locator) -> None:
        """
        Clear input field

        Args:
            locator: Element locator
        """
        element = self._get_element(locator)
        element.clear()

    def get_text(self, locator: str | Locator, timeout: Optional[int] = None) -> str:
        """
        Get text content of an element

        Args:
            locator: Element locator
            timeout: Custom timeout in milliseconds

        Returns:
            Text content of the element
        """
        timeout = timeout or self.timeout
        element = self._get_element(locator)
        text = element.text_content(timeout=timeout)
        self.logger.debug("Text from element %s: %s", locator, text)
        return text.strip() if text else ""

    def get_attribute(self, locator: str | Locator, attribute: str) -> str | None:
        """
        Get attribute value of an element

        Args:
            locator: Element locator
            attribute: Attribute name

        Returns:
            Attribute value or None
        """
        element = self._get_element(locator)
        value = element.get_attribute(attribute)
        self.logger.debug("Attribute '%s' from element %s: %s", attribute, locator, value)
        return value

    def is_visible(self, locator: str | Locator, timeout: Optional[int] = None) -> bool:
        """
        Check if element is visible

        Args:
            locator: Element locator
            timeout: Custom timeout in milliseconds

        Returns:
            True if visible, False otherwise
        """
        timeout = timeout or self.timeout
        try:
            element = self._get_element(locator)
            result = element.is_visible(timeout=timeout)
            self.logger.debug("Element %s visible: %s", locator, result)
            return result
        except (TimeoutError, Error):
            return False

    def is_enabled(self, locator: str | Locator) -> bool:
        """
        Check if element is enabled

        Args:
            locator: Element locator

        Returns:
            True if enabled, False otherwise
        """
        element = self._get_element(locator)
        result = element.is_enabled()
        self.logger.debug("Element %s enabled: %s", locator, result)
        return result

    def wait_for_element(
        self,
        locator: str | Locator,
        state: str = "visible",
        timeout: Optional[int] = None
    ) -> None:
        """
        Wait for element to be in a specific state

        Args:
            locator: Element locator
            state: State to wait for ('attached', 'detached', 'visible', 'hidden')
            timeout: Custom timeout in milliseconds
        """
        timeout = timeout or self.timeout
        element = self._get_element(locator)
        self.logger.info("Waiting for element %s to be %s", locator, state)
        element.wait_for(state=state, timeout=timeout)

    def wait_for_url(self, url_pattern: str, timeout: Optional[int] = None) -> None:
        """
        Wait for URL to match pattern

        Args:
            url_pattern: URL pattern to match
            timeout: Custom timeout in milliseconds
        """
        timeout = timeout or self.timeout
        self.logger.info("Waiting for URL to match: %s", url_pattern)
        self.page.wait_for_url(url_pattern, timeout=timeout)

    def select_option(self, locator: str | Locator, value: str) -> None:
        """
        Select option from dropdown

        Args:
            locator: Element locator
            value: Value to select
        """
        element = self._get_element(locator)
        self.logger.info("Selecting option '%s' from dropdown: %s", value, locator)
        element.select_option(value)

    def check(self, locator: str | Locator) -> None:
        """
        Check a checkbox or radio button

        Args:
            locator: Element locator
        """
        element = self._get_element(locator)
        self.logger.info("Checking element: %s", locator)
        element.check()

    def uncheck(self, locator: str | Locator) -> None:
        """
        Uncheck a checkbox

        Args:
            locator: Element locator
        """
        element = self._get_element(locator)
        self.logger.info("Unchecking element: %s", locator)
        element.uncheck()

    def hover(self, locator: str | Locator) -> None:
        """
        Hover over an element

        Args:
            locator: Element locator
        """
        element = self._get_element(locator)
        self.logger.info("Hovering over element: %s", locator)
        element.hover()

    def scroll_to(self, locator: str | Locator) -> None:
        """
        Scroll to element

        Args:
            locator: Element locator
        """
        element = self._get_element(locator)
        self.logger.info("Scrolling to element: %s", locator)
        element.scroll_into_view_if_needed()

    def get_all_elements(self, locator: str) -> List[Locator]:
        """
        Get all elements matching locator

        Args:
            locator: Element locator

        Returns:
            List of Locator objects
        """
        elements = self.page.locator(locator).all()
        self.logger.debug("Found %d elements for locator: %s", len(elements), locator)
        return elements

    def get_element_count(self, locator: str) -> int:
        """
        Get count of elements matching locator

        Args:
            locator: Element locator

        Returns:
            Number of matching elements
        """
        count = self.page.locator(locator).count()
        self.logger.debug("Element count for %s: %d", locator, count)
        return count

    def press_key(self, key: str) -> None:
        """
        Press a keyboard key

        Args:
            key: Key to press (e.g., 'Enter', 'Escape', 'Tab')
        """
        self.logger.info("Pressing key: %s", key)
        self.page.keyboard.press(key)

    def take_screenshot(self, path: str, full_page: bool = False) -> None:
        """
        Take a screenshot

        Args:
            path: Path to save screenshot
            full_page: Whether to capture full page
        """
        self.logger.info("Taking screenshot: %s", path)
        self.page.screenshot(path=path, full_page=full_page)

    def switch_to_frame(self, frame_locator: str) -> None:
        """
        Switch to iframe

        Args:
            frame_locator: Frame locator
        """
        self.logger.info("Switching to frame: %s", frame_locator)
        self.page.frame_locator(frame_locator)

    def execute_javascript(self, script: str, *args) -> any:
        """
        Execute JavaScript code

        Args:
            script: JavaScript code to execute
            *args: Arguments to pass to the script

        Returns:
            Result of JavaScript execution
        """
        self.logger.info("Executing JavaScript: %s", script)
        return self.page.evaluate(script, *args)

    def reload(self) -> None:
        """Reload the current page"""
        self.logger.info("Reloading page")
        self.page.reload()

    def go_back(self) -> None:
        """Navigate back in browser history"""
        self.logger.info("Navigating back")
        self.page.go_back()

    def go_forward(self) -> None:
        """Navigate forward in browser history"""
        self.logger.info("Navigating forward")
        self.page.go_forward()

    # Assertion Methods
    def assert_element_visible(self, locator: str | Locator) -> None:
        """Assert element is visible"""
        element = self._get_element(locator)
        expect(element).to_be_visible(timeout=self.timeout)
        self.logger.info("Assertion passed: Element %s is visible", locator)

    def assert_element_hidden(self, locator: str | Locator) -> None:
        """Assert element is hidden"""
        element = self._get_element(locator)
        expect(element).to_be_hidden(timeout=self.timeout)
        self.logger.info("Assertion passed: Element %s is hidden", locator)

    def assert_text_equals(self, locator: str | Locator, expected_text: str) -> None:
        """Assert element text equals expected text"""
        element = self._get_element(locator)
        expect(element).to_have_text(expected_text, timeout=self.timeout)
        self.logger.info("Assertion passed: Text equals '%s'", expected_text)

    def assert_text_contains(self, locator: str | Locator, expected_text: str) -> None:
        """Assert element text contains expected text"""
        element = self._get_element(locator)
        expect(element).to_contain_text(expected_text, timeout=self.timeout)
        self.logger.info("Assertion passed: Text contains '%s'", expected_text)

    def assert_url_contains(self, expected_url: str) -> None:
        """Assert URL contains expected string"""
        expect(self.page).to_have_url(f"**{expected_url}**", timeout=self.timeout)
        self.logger.info("Assertion passed: URL contains '%s'", expected_url)

    def assert_title_contains(self, expected_title: str) -> None:
        """Assert page title contains expected string"""
        expect(self.page).to_have_title(f"**{expected_title}**", timeout=self.timeout)
        self.logger.info("Assertion passed: Title contains '%s'", expected_title)
