"""
Pytest Configuration and Fixtures
Central configuration for all tests
"""
from typing import Generator

import pytest
from playwright.sync_api import Page, BrowserContext

from utils.config_reader import config
from utils.logger import get_logger
from utils.helpers import create_directory, get_timestamp

# Optional allure import
try:
    import allure
    ALLURE_AVAILABLE = True
except ImportError:
    ALLURE_AVAILABLE = False

logger = get_logger(__name__)


def pytest_configure(config):
    """Pytest configuration hook"""
    # Create necessary directories
    create_directory("reports")
    create_directory("screenshots")
    create_directory("traces")
    create_directory("logs")
    logger.info("Test session started")


def pytest_unconfigure(config):
    """Pytest unconfiguration hook"""
    logger.info("Test session ended")


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_name: str):
    """
    Browser launch arguments (browser-specific)
    
    Args:
        browser_name: Name of the browser (chromium, firefox, webkit)
    
    Returns:
        Dict with browser launch arguments
    """
    # Base arguments
    launch_args = {
        "headless": config.headless,
        "slow_mo": config.slow_mo,
    }
    
    # Add browser-specific arguments
    if browser_name == "chromium":
        launch_args["args"] = [
            "--disable-blink-features=AutomationControlled",
            "--disable-dev-shm-usage",
        ]
    elif browser_name == "firefox":
        # Firefox-specific arguments
        launch_args["args"] = []
    elif browser_name == "webkit":
        # WebKit doesn't support many custom args
        launch_args["args"] = []
    
    return launch_args


@pytest.fixture(scope="session")
def browser_context_args(browser_name: str):
    """
    Browser context arguments (browser-specific)
    
    Args:
        browser_name: Name of the browser (chromium, firefox, webkit)
        
    Returns:
        Dict with browser context arguments
    """
    context_args = {
        "viewport": {"width": 1920, "height": 1080},
        "locale": "en-US",
        "timezone_id": "America/New_York",
    }
    
    # Only set custom user agent for Chromium
    # Firefox and WebKit have their own default user agents
    if browser_name == "chromium":
        context_args["user_agent"] = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    
    return context_args


@pytest.fixture(scope="function")
def page(context: BrowserContext, request) -> Generator[Page, None, None]:
    """
    Create a new page for each test

    Args:
        context: Browser context fixture
        request: Pytest request object

    Yields:
        Page object
    """
    logger.info("Creating new page for test: %s", request.node.name)

    # Start tracing if enabled
    if config.trace_on_failure:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Create new page
    test_page = context.new_page()

    # Run test
    yield test_page

    # Post-test actions
    _handle_test_completion(test_page, context, request)


def _handle_test_completion(
    test_page: Page,
    context: BrowserContext,
    request
) -> None:
    """
    Handle test completion (screenshot, trace, cleanup)

    Args:
        test_page: Page object
        context: Browser context
        request: Pytest request object
    """
    # Get test result
    if not hasattr(request.node, 'rep_call'):
        return

    # Handle test failure
    if request.node.rep_call.failed:
        logger.error("Test FAILED: %s", request.node.name)

        # Take screenshot on failure
        if config.screenshot_on_failure:
            screenshot_dir = create_directory("screenshots")
            screenshot_name = f"{request.node.name}_{get_timestamp()}.png"
            screenshot_path = screenshot_dir / screenshot_name
            test_page.screenshot(path=str(screenshot_path), full_page=True)
            logger.info("Screenshot saved: %s", screenshot_path)

            # Attach to Allure report if available
            if ALLURE_AVAILABLE:
                allure.attach.file(
                    str(screenshot_path),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

        # Save trace on failure
        if config.trace_on_failure:
            trace_dir = create_directory("traces")
            trace_name = f"{request.node.name}_{get_timestamp()}.zip"
            trace_path = trace_dir / trace_name
            context.tracing.stop(path=str(trace_path))
            logger.info("Trace saved: %s", trace_path)

            # Attach to Allure report if available
            if ALLURE_AVAILABLE:
                with open(trace_path, 'rb') as trace_file:
                    allure.attach(
                        trace_file.read(),
                        name="Trace",
                        attachment_type="application/zip",
                        extension=".zip"
                    )
    else:
        logger.info("Test PASSED: %s", request.node.name)
        if config.trace_on_failure:
            context.tracing.stop()

    test_page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results

    Args:
        item: Test item
        call: Test call
    """
    outcome = yield
    rep = outcome.get_result()

    # Store test result in item for later access
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="function", autouse=True)
def log_test_info(request):
    """
    Log test information

    Args:
        request: Pytest request object
    """
    logger.info("=" * 80)
    logger.info("Starting test: %s", request.node.name)
    logger.info("Test file: %s", request.node.fspath)
    logger.info("=" * 80)

    yield

    logger.info("Finished test: %s", request.node.name)
