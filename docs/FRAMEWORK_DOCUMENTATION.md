# Test Automation Framework Documentation

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Core Components](#core-components)
6. [Page Objects](#page-objects)
7. [Test Suite](#test-suite)
8. [Configuration](#configuration)
9. [Utilities](#utilities)
10. [Reporting](#reporting)
11. [Best Practices](#best-practices)
12. [Setup & Installation](#setup--installation)
13. [Running Tests](#running-tests)
14. [CI/CD Integration](#cicd-integration)
15. [Troubleshooting](#troubleshooting)

---

## Overview

This is an enterprise-grade test automation framework built for testing https://ultimateqa.com/automation using Playwright and Python. The framework follows the Page Object Model (POM) design pattern and incorporates industry best practices for maintainability, scalability, and reliability.

### Key Features
- **Page Object Model (POM)**: Separation of test logic from page interactions
- **Reusable Base Page**: 40+ common methods for element interactions
- **Multiple Reporting**: Allure, HTML, and pytest reports
- **Configurable Execution**: Environment-based configuration via .env
- **Comprehensive Logging**: Colored console output with file logging
- **Screenshot & Trace Capture**: Automatic capture on test failures
- **Test Data Management**: YAML and JSON-based test data with Faker integration
- **Parallel Execution**: Support for pytest-xdist
- **Multiple Browser Support**: Chromium, Firefox, WebKit via Playwright

---

## Architecture

### Design Pattern: Page Object Model (POM)

```
┌─────────────────────────────────────────────────────────────┐
│                        Test Layer                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │ test_smoke  │  │test_regress │  │  test_api   │         │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘         │
└─────────┼─────────────────┼─────────────────┼───────────────┘
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
┌───────────────────────────┼───────────────────────────────┐
│                    Page Object Layer                       │
│  ┌─────────────────────────────────────────────────────┐  │
│  │              AutomationPage                          │  │
│  │  - Locators (BIG_PAGE_LINK, etc.)                   │  │
│  │  - Methods (navigate(), click_big_page_link())      │  │
│  └───────────────────────┬─────────────────────────────┘  │
│                          │ inherits                        │
│  ┌───────────────────────┴─────────────────────────────┐  │
│  │              BasePage                                │  │
│  │  - 40+ reusable methods                             │  │
│  │  - click(), fill(), wait_for(), assert_*()          │  │
│  └─────────────────────────────────────────────────────┘  │
└────────────────────────────┬──────────────────────────────┘
                             │
┌────────────────────────────┼──────────────────────────────┐
│                     Utility Layer                          │
│  ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌───────────┐     │
│  │ Logger  │ │  Config  │ │TestData  │ │ Helpers   │     │
│  └─────────┘ └──────────┘ └──────────┘ └───────────┘     │
└────────────────────────────────────────────────────────────┘
```

### Framework Flow

1. **Test Initialization**
   - pytest collects tests
   - conftest.py fixtures initialize browser and page
   - Configuration loaded from .env and pytest.ini

2. **Test Execution**
   - Test uses Page Object to interact with UI
   - Page Object uses BasePage methods
   - BasePage communicates with Playwright API
   - Logger records all actions
   - Screenshots/traces captured on failure

3. **Test Reporting**
   - pytest generates results
   - Allure collects test metadata
   - HTML report generated
   - Screenshots/traces attached to reports

---

## Technology Stack

### Core Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.14.0 | Programming language |
| Playwright | 1.48.0 | Browser automation |
| Pytest | 8.4.2 | Test framework |
| Allure | 2.35.1 | Advanced reporting |

### Supporting Libraries
| Library | Version | Purpose |
|---------|---------|---------|
| pytest-playwright | 0.7.1 | Pytest-Playwright integration |
| allure-pytest | 2.15.0 | Allure-pytest integration |
| pytest-html | 4.1.1 | HTML report generation |
| pytest-xdist | 3.8.0 | Parallel test execution |
| faker | 37.11.0 | Test data generation |
| pyyaml | 6.0.2 | YAML file parsing |
| python-dotenv | 1.0.1 | Environment variable management |

---

## Project Structure

```
SDET playwright python/
├── pages/                          # Page Object Models
│   ├── __init__.py                 # Package initializer
│   ├── base_page.py                # Base page with 40+ reusable methods
│   └── automation_page.py          # AutomationPage object
│
├── tests/                          # Test suites
│   ├── __init__.py                 # Package initializer
│   ├── conftest.py                 # Pytest fixtures & configuration
│   ├── test_smoke.py               # Smoke tests (critical path)
│   ├── test_regression.py          # Regression tests (comprehensive)
│   └── test_api.py                 # API tests (placeholder)
│
├── utils/                          # Utility modules
│   ├── __init__.py                 # Package initializer
│   ├── logger.py                   # Colored logging system
│   ├── config_reader.py            # Configuration management
│   ├── test_data.py                # Test data management
│   └── helpers.py                  # Helper functions
│
├── test_data/                      # Test data files
│   ├── test_scenarios.yaml         # Test scenarios data
│   └── test_users.json             # User test data
│
├── reports/                        # Test reports
│   ├── allure-report/              # Allure HTML report
│   ├── allure-results/             # Allure raw results
│   └── html/                       # Pytest HTML report
│
├── screenshots/                    # Failure screenshots
├── traces/                         # Playwright traces
├── videos/                         # Test execution videos (if enabled)
├── logs/                           # Application logs
│
├── .env                            # Environment variables
├── .env.example                    # Example environment file
├── .gitignore                      # Git ignore rules
├── .pylintrc                       # Pylint configuration
├── pytest.ini                      # Pytest configuration
├── pyproject.toml                  # Python project configuration
├── requirements.txt                # Python dependencies
├── README.md                       # Quick start guide
├── FRAMEWORK_DOCUMENTATION.md      # This file
├── QUICKSTART.md                   # Quick start guide
├── ARCHITECTURE.md                 # Architecture details
└── setup.sh / setup.bat            # Setup scripts
```

---

## Core Components

### 1. BasePage (`pages/base_page.py`)

The foundation of the framework, providing 40+ reusable methods for interacting with web elements.

#### Key Features:
- **Element Interactions**: click, fill, select, hover, drag-and-drop
- **Waits & Synchronization**: Smart waits for various element states
- **Assertions**: Built-in assertion methods
- **Navigation**: URL handling and page navigation
- **JavaScript Execution**: Execute custom scripts
- **Screenshots**: Capture element or full-page screenshots
- **Keyboard/Mouse**: Advanced input handling

#### Method Categories:

**Navigation Methods**
```python
navigate(url)                    # Navigate to URL
go_back()                        # Browser back
go_forward()                     # Browser forward
refresh()                        # Refresh page
get_url()                        # Get current URL
get_title()                      # Get page title
```

**Element Interaction Methods**
```python
click(locator)                   # Click element
double_click(locator)            # Double-click element
right_click(locator)             # Right-click element
fill(locator, text)              # Fill input field
clear(locator)                   # Clear input field
select_option(locator, value)    # Select dropdown option
check(locator)                   # Check checkbox
uncheck(locator)                 # Uncheck checkbox
hover(locator)                   # Hover over element
drag_and_drop(source, target)    # Drag and drop
```

**Wait Methods**
```python
wait_for_element(locator, state)        # Wait for element state
wait_for_url(pattern, timeout)          # Wait for URL pattern
wait_for_load_state(state)              # Wait for page load state
wait_for_timeout(milliseconds)          # Hard wait
```

**Assertion Methods**
```python
assert_element_visible(locator)         # Assert element is visible
assert_element_hidden(locator)          # Assert element is hidden
assert_text_equals(locator, expected)   # Assert exact text match
assert_text_contains(locator, expected) # Assert text contains
assert_url_contains(text)               # Assert URL contains text
```

**Information Retrieval Methods**
```python
get_text(locator)                # Get element text
get_attribute(locator, name)     # Get attribute value
get_element_count(locator)       # Count matching elements
is_visible(locator)              # Check if visible
is_enabled(locator)              # Check if enabled
is_checked(locator)              # Check if checked
```

**Advanced Methods**
```python
execute_script(script)           # Execute JavaScript
scroll_to_element(locator)       # Scroll element into view
take_screenshot(path)            # Capture screenshot
press_key(locator, key)          # Press keyboard key
upload_file(locator, path)       # Upload file
```

#### Example Usage:
```python
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = "#username"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    
    def login(self, username, password):
        self.fill(self.USERNAME_FIELD, username)
        self.fill(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        self.wait_for_url("**/dashboard")
```

### 2. Configuration Management (`utils/config_reader.py`)

Singleton-based configuration reader supporting multiple file formats.

#### Features:
- Singleton pattern for consistent configuration access
- Support for .env, .json, .yaml files
- Environment variable override capability
- Type conversion and validation
- Default value handling

#### Configuration Structure (.env):
```bash
# Application Settings
BASE_URL=https://ultimateqa.com/automation
APP_ENV=staging

# Browser Settings
BROWSER=chromium              # chromium, firefox, webkit
HEADLESS=false                # true/false
SLOW_MO=0                     # milliseconds delay

# Timeout Settings
DEFAULT_TIMEOUT=30000         # milliseconds
NAVIGATION_TIMEOUT=60000      # milliseconds
ASSERTION_TIMEOUT=10000       # milliseconds

# Screenshot Settings
SCREENSHOT_ON_FAILURE=true
VIDEO_ON_FAILURE=false
TRACE_ON_FAILURE=true

# Logging Settings
LOG_LEVEL=INFO                # DEBUG, INFO, WARNING, ERROR
LOG_TO_FILE=true
LOG_FILE_PATH=logs/test.log
```

#### Usage Example:
```python
from utils.config_reader import ConfigReader

config = ConfigReader()
base_url = config.get("BASE_URL")
timeout = config.get("DEFAULT_TIMEOUT", 30000)  # with default
is_headless = config.get("HEADLESS") == "true"
```

### 3. Logging System (`utils/logger.py`)

Colored, structured logging with file and console output.

#### Features:
- Color-coded log levels (INFO=Cyan, WARNING=Yellow, ERROR=Red)
- Automatic log rotation
- Contextual logging (test name, file name)
- Performance tracking
- Lazy evaluation for efficiency

#### Log Levels:
```python
logger.debug("Detailed debug information")
logger.info("General information")
logger.warning("Warning message")
logger.error("Error occurred")
logger.critical("Critical error")
```

#### Log Format:
```
2025-10-23 18:26:12 [    INFO] Starting test: test_page_loads_successfully
2025-10-23 18:26:13 [    INFO] Navigating to: https://ultimateqa.com/automation
2025-10-23 18:26:14 [    INFO] Waiting for element h1 to be visible
2025-10-23 18:26:15 [    INFO] Clicking element: a:has-text('Big Page')
2025-10-23 18:26:16 [    INFO] Test PASSED: test_page_loads_successfully
```

### 4. Test Data Management (`utils/test_data.py`)

Dynamic test data generation and management using Faker.

#### Features:
- Faker integration for realistic data
- Data classes for type safety
- YAML/JSON data file support
- Parameterization support

#### Example Data Class:
```python
from dataclasses import dataclass
from faker import Faker

fake = Faker()

@dataclass
class ContactFormData:
    name: str
    email: str
    phone: str
    message: str
    
    @classmethod
    def generate(cls):
        return cls(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            message=fake.text(max_nb_chars=200)
        )
```

#### YAML Data Example (`test_data/test_scenarios.yaml`):
```yaml
login_scenarios:
  valid_login:
    username: "test_user"
    password: "Test@123"
    expected: "success"
  
  invalid_login:
    username: "invalid_user"
    password: "wrong_pass"
    expected: "error"

navigation_links:
  - name: "Big Page"
    url: "complicated-page"
  - name: "Fake Landing"
    url: "fake-landing-page"
  - name: "Fake Pricing"
    url: "fake-pricing-page"
```

---

## Page Objects

### AutomationPage (`pages/automation_page.py`)

Page object for the UltimateQA automation practice page.

#### Locator Strategy
The page uses Playwright's modern locator strategies:
```python
# Text-based locators (robust to UI changes)
BIG_PAGE_LINK = "a:has-text('Big page with many elements')"
FAKE_LANDING_PAGE_LINK = "a:has-text('Fake Landing Page')"

# Attribute-based locators
LINKEDIN_ICON = "a[href*='linkedin']"
TWITTER_ICON = "a[href*='twitter']"

# Tag-based locators
PAGE_TITLE = "h1"
PAGE_HEADING = "h1:has-text('Automation Practice')"
```

#### Available Methods

**Navigation:**
```python
navigate(url=None)                      # Navigate to page
verify_page_loaded()                    # Verify page loaded
```

**Link Interactions:**
```python
click_big_page_link()                   # Navigate to big page
click_fake_landing_page_link()          # Navigate to landing page
click_fake_pricing_page_link()          # Navigate to pricing page
```

**Visibility Checks:**
```python
is_big_page_link_visible()              # Check link visibility
is_fake_landing_page_link_visible()     # Check link visibility
is_twitter_icon_visible()               # Check icon visibility
is_facebook_icon_visible()              # Check icon visibility
is_linkedin_icon_visible()              # Check icon visibility
```

**Composite Checks:**
```python
has_navigation_links()                  # Check all nav links present
has_social_media_icons()                # Check social icons present
```

**Information Retrieval:**
```python
get_page_heading_text()                 # Get main heading text
```

---

## Test Suite

### Test Organization

Tests are organized into three categories:

1. **Smoke Tests** (`test_smoke.py`)
   - Critical path validation
   - Quick execution (< 1 minute)
   - Run before every deployment
   - Must pass 100% for release

2. **Regression Tests** (`test_regression.py`)
   - Comprehensive feature testing
   - Longer execution time
   - Run on schedule (nightly)
   - Cover all user scenarios

3. **API Tests** (`test_api.py`)
   - API endpoint validation
   - Currently placeholder
   - Future expansion planned

### Test Markers

```python
@pytest.mark.smoke          # Smoke test
@pytest.mark.regression     # Regression test
@pytest.mark.critical       # Critical functionality
@pytest.mark.skip           # Skip test
@pytest.mark.xfail          # Expected failure
@pytest.mark.parametrize    # Parameterized test
```

### Test Structure Example

```python
import pytest
from pages.automation_page import AutomationPage

@pytest.mark.smoke
@pytest.mark.critical
class TestBasicFunctionality:
    """Basic smoke tests for critical functionality"""
    
    def test_page_loads_successfully(self, page):
        """Test that the automation page loads successfully"""
        # Arrange
        automation_page = AutomationPage(page)
        
        # Act
        automation_page.navigate()
        
        # Assert
        assert automation_page.verify_page_loaded()
        assert "automation" in page.url.lower()
```

### Fixtures (`tests/conftest.py`)

#### Session-Scoped Fixtures:
```python
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "user_agent": "Custom User Agent",
    }
```

#### Function-Scoped Fixtures:
```python
@pytest.fixture
def page(context, request):
    """Create new page for each test"""
    page = context.new_page()
    # Setup tracing, screenshots
    yield page
    # Teardown and cleanup
```

#### Hook Functions:
```python
def pytest_configure(config):
    """Register custom markers"""
    
def pytest_runtest_setup(item):
    """Before each test"""
    
def pytest_runtest_teardown(item):
    """After each test"""
```

---

## Configuration

### pytest.ini

```ini
[pytest]
# Test discovery
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# Markers
markers =
    smoke: Quick smoke tests
    regression: Comprehensive regression tests
    critical: Critical path tests
    api: API tests

# Reporting
addopts =
    -v
    --tb=short
    --strict-markers
    --alluredir=reports/allure-results
    --html=reports/html/report.html
    --self-contained-html

# Logging
log_cli = true
log_cli_level = INFO
log_file = logs/pytest.log
log_file_level = DEBUG
```

### .env Configuration

```bash
# Base URL
BASE_URL=https://ultimateqa.com/automation

# Browser Settings
BROWSER=chromium
HEADLESS=false
SLOW_MO=0

# Timeouts (milliseconds)
DEFAULT_TIMEOUT=30000
NAVIGATION_TIMEOUT=60000
ASSERTION_TIMEOUT=10000

# Screenshots & Videos
SCREENSHOT_ON_FAILURE=true
VIDEO_ON_FAILURE=false
TRACE_ON_FAILURE=true

# Logging
LOG_LEVEL=INFO
LOG_TO_FILE=true
```

---

## Reporting

### 1. Allure Reports

**Features:**
- Timeline view of test execution
- Historical trends
- Test categorization
- Attachment support (screenshots, videos, traces)
- Detailed step logs
- Environment information

**Generate Report:**
```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

**Serve Report:**
```bash
allure serve reports/allure-results
# OR
python -m http.server 8080 -d reports/allure-report
```

**Report Sections:**
- **Overview**: Pass/fail statistics, duration, trends
- **Categories**: Test categorization by feature
- **Suites**: Test suite organization
- **Graphs**: Visual representation of results
- **Timeline**: Execution timeline
- **Behaviors**: BDD-style behavior organization
- **Packages**: Test package structure

### 2. HTML Reports

**Features:**
- Self-contained HTML file
- Screenshots embedded
- Collapsible sections
- Filter capabilities
- Sortable columns

**Generated automatically at:**
```
reports/html/report.html
```

### 3. Pytest Console Output

**Features:**
- Real-time test execution
- Color-coded results
- Progress indicators
- Failure details
- Execution time

---

## Best Practices

### 1. Locator Strategy

**Priority Order:**
1. User-facing text: `"button:has-text('Submit')"`
2. Accessible attributes: `"[aria-label='Search']"`
3. Data test IDs: `"[data-testid='login-button']"`
4. Semantic IDs: `"#submit-button"`
5. CSS classes (last resort): `".btn-primary"`

**Avoid:**
- XPath unless necessary
- Brittle CSS selectors
- Index-based selection

### 2. Test Independence

Each test should:
- Set up its own data
- Clean up after itself
- Not depend on other tests
- Be runnable in isolation
- Be runnable in any order

### 3. Assertion Strategy

**Good:**
```python
assert automation_page.is_visible(locator), "Element should be visible"
assert "expected" in actual_text, f"Expected text not found. Actual: {actual_text}"
```

**Avoid:**
```python
assert True  # Meaningless
assert element  # No context
```

### 4. Wait Strategy

**Prefer:**
```python
page.wait_for_selector(locator, state="visible")
page.wait_for_url("**/dashboard")
```

**Avoid:**
```python
time.sleep(5)  # Hard waits
```

### 5. Error Handling

```python
try:
    automation_page.click(locator)
except TimeoutError:
    logger.error(f"Element not found: {locator}")
    # Take screenshot
    # Re-raise or handle gracefully
    raise
```

---

## Setup & Installation

### Prerequisites
- Python 3.10+
- pip (Python package manager)
- Git

### Installation Steps

1. **Clone Repository:**
```bash
git clone <repository-url>
cd "SDET playwright python"
```

2. **Create Virtual Environment:**
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Install Playwright Browsers:**
```bash
python -m playwright install
```

5. **Configure Environment:**
```bash
cp .env.example .env
# Edit .env with your settings
```

6. **Verify Installation:**
```bash
python -m pytest --version
python -m playwright --version
```

---

## Running Tests

### Basic Execution

**Run all tests:**
```bash
python -m pytest tests/
```

**Run specific test file:**
```bash
python -m pytest tests/test_smoke.py
```

**Run specific test:**
```bash
python -m pytest tests/test_smoke.py::TestBasicFunctionality::test_page_loads_successfully
```

### With Markers

**Run smoke tests only:**
```bash
python -m pytest -m smoke
```

**Run critical tests:**
```bash
python -m pytest -m critical
```

**Run multiple markers:**
```bash
python -m pytest -m "smoke or regression"
```

### Verbose Output

```bash
python -m pytest -v          # Verbose
python -m pytest -vv         # More verbose
python -m pytest -s          # Show print statements
```

### Parallel Execution

```bash
python -m pytest -n 4        # Run on 4 CPU cores
python -m pytest -n auto     # Auto-detect cores
```

### Browser Selection

```bash
python -m pytest --browser chromium
python -m pytest --browser firefox
python -m pytest --browser webkit
python -m pytest --browser chromium --browser firefox  # Multiple
```

### Headed Mode

```bash
python -m pytest --headed     # Show browser
python -m pytest --slowmo 100 # Slow down by 100ms
```

### Stop on First Failure

```bash
python -m pytest -x           # Stop on first failure
python -m pytest --maxfail=3  # Stop after 3 failures
```

### Generate Reports

```bash
# With Allure
python -m pytest --alluredir=reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean

# With HTML
python -m pytest --html=reports/html/report.html --self-contained-html
```

### Combined Example

```bash
python -m pytest tests/ \
  -v \
  -n auto \
  --browser chromium \
  --headed \
  -m smoke \
  --alluredir=reports/allure-results \
  --html=reports/html/report.html
```

---

## CI/CD Integration

### GitHub Actions

Example workflow file (`.github/workflows/tests.yml`):

```yaml
name: Automated Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        browser: [chromium, firefox, webkit]
        python-version: ['3.10', '3.11', '3.12']
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        python -m playwright install --with-deps
    
    - name: Run tests
      run: |
        python -m pytest tests/ \
          --browser ${{ matrix.browser }} \
          --alluredir=reports/allure-results \
          --html=reports/html/report.html
      env:
        BASE_URL: ${{ secrets.BASE_URL }}
        HEADLESS: true
    
    - name: Generate Allure Report
      if: always()
      run: |
        allure generate reports/allure-results -o reports/allure-report
    
    - name: Upload Allure Results
      if: always()
      uses: actions/upload-artifact@v3
      with:
        name: allure-results-${{ matrix.browser }}
        path: reports/allure-results
    
    - name: Upload Screenshots
      if: failure()
      uses: actions/upload-artifact@v3
      with:
        name: screenshots-${{ matrix.browser }}
        path: screenshots/
```

### Jenkins Pipeline

```groovy
pipeline {
    agent any
    
    environment {
        BASE_URL = credentials('base-url')
        HEADLESS = 'true'
    }
    
    stages {
        stage('Setup') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
                sh '. venv/bin/activate && python -m playwright install'
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest tests/ \
                        -n auto \
                        --alluredir=reports/allure-results \
                        --html=reports/html/report.html
                '''
            }
        }
        
        stage('Report') {
            steps {
                allure includeProperties: false,
                       jdk: '',
                       results: [[path: 'reports/allure-results']]
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'screenshots/*, reports/**/*',
                           allowEmptyArchive: true
            
            publishHTML([
                reportDir: 'reports/html',
                reportFiles: 'report.html',
                reportName: 'HTML Test Report'
            ])
        }
    }
}
```

---

## Troubleshooting

### Common Issues

#### 1. Playwright Browsers Not Installed
**Error:** `Executable doesn't exist at ...`
**Solution:**
```bash
python -m playwright install
```

#### 2. Import Errors
**Error:** `ModuleNotFoundError: No module named 'pages'`
**Solution:**
```bash
# Ensure you're in the project root directory
export PYTHONPATH="${PYTHONPATH}:$(pwd)"  # Linux/Mac
$env:PYTHONPATH += ";$(pwd)"              # Windows PowerShell
```

#### 3. Test Timeout Issues
**Error:** `TimeoutError: Timeout 30000ms exceeded`
**Solution:**
- Increase timeout in `.env`: `DEFAULT_TIMEOUT=60000`
- Check network connectivity
- Verify locator is correct

#### 4. Allure Command Not Found
**Error:** `allure: command not found`
**Solution:**
```bash
# Install via Scoop (Windows)
scoop install allure

# Install via Homebrew (Mac)
brew install allure

# Install via apt (Linux)
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

#### 5. Tests Fail in Headless Mode
**Issue:** Tests pass when headed but fail when headless
**Solution:**
- Add `page.wait_for_load_state("networkidle")` after navigation
- Increase timeouts for CI/CD environments
- Check for viewport size issues
- Verify element visibility with screenshots

#### 6. Parallel Execution Conflicts
**Issue:** Tests fail when run in parallel
**Solution:**
- Ensure test independence
- Use unique test data per test
- Avoid shared state
- Use database transactions or test-specific data

### Debug Mode

**Enable detailed logging:**
```bash
export DEBUG=pw:api  # Linux/Mac
$env:DEBUG = "pw:api"  # Windows PowerShell
```

**Run with pytest debugging:**
```bash
python -m pytest --pdb  # Drop to debugger on failure
python -m pytest -vv -s  # Verbose with output
```

**Enable Playwright Inspector:**
```bash
python -m pytest --headed --slowmo=1000
```

---

## Maintenance

### Regular Tasks

**Weekly:**
- Review and update failing tests
- Check for outdated dependencies
- Review test execution time

**Monthly:**
- Update dependencies: `pip list --outdated`
- Review and refactor flaky tests
- Update documentation

**Quarterly:**
- Major dependency updates
- Framework architecture review
- Performance optimization

### Dependency Updates

```bash
# Check outdated packages
pip list --outdated

# Update specific package
pip install --upgrade playwright

# Update all packages
pip install --upgrade -r requirements.txt

# Update Playwright browsers
python -m playwright install
```

---

## Performance Optimization

### Tips for Faster Execution

1. **Parallel Execution:**
```bash
python -m pytest -n auto
```

2. **Browser Context Reuse:**
```python
@pytest.fixture(scope="session")
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()
```

3. **Skip Unnecessary Waits:**
```python
# Bad
time.sleep(5)

# Good
page.wait_for_selector(locator, state="visible")
```

4. **Optimize Locators:**
- Use specific locators
- Avoid `//` XPath axes
- Use CSS selectors when possible

5. **Minimize Screenshot/Video Capture:**
```python
# Only on failure
screenshot_on_failure=True
video_on_failure=False
```

---

## Security Considerations

### Sensitive Data Handling

1. **Never commit sensitive data:**
   - Use `.env` for secrets
   - Add `.env` to `.gitignore`
   - Use CI/CD secret management

2. **Mask sensitive data in logs:**
```python
def login(self, username, password):
    self.logger.info(f"Logging in as: {username}")
    self.logger.info("Password: ********")  # Never log actual password
```

3. **Use environment-specific configurations:**
```bash
# .env.staging
BASE_URL=https://staging.example.com

# .env.production
BASE_URL=https://example.com
```

---

## Contributing Guidelines

### Code Style

Follow PEP 8 with these additions:
- Line length: 120 characters
- Use type hints where appropriate
- Document all public methods
- Use meaningful variable names

### Pull Request Process

1. Create feature branch from `develop`
2. Write/update tests
3. Update documentation
4. Run linters: `pylint pages/ tests/ utils/`
5. Ensure all tests pass
6. Submit PR with description

### Commit Messages

Format: `<type>(<scope>): <subject>`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Example:
```
feat(pages): Add login page object
fix(tests): Fix flaky timeout in test_navigation
docs(readme): Update installation instructions
```

---

## Support & Resources

### Documentation
- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Documentation](https://docs.qameta.io/allure/)

### Community
- Playwright Discord
- Stack Overflow (`playwright` tag)
- GitHub Issues

### Internal Contacts
- Framework Maintainer: [Your Name]
- QA Lead: [Lead Name]
- DevOps Support: [DevOps Contact]

---

**Document Version:** 1.0  
**Last Updated:** October 23, 2025  
**Framework Version:** 1.0.0
