# Test Automation Framework - Ultimate QA

A professional-grade test automation framework built with Playwright and Python, following industry best practices and design patterns.

## 🏗️ Framework Architecture

```
playwright-python-framework/
│
├── pages/                      # Page Object Models
│   ├── base_page.py           # Base page with common methods
│   └── automation_page.py     # Specific page objects
│
├── tests/                     # Test cases
│   ├── conftest.py           # Pytest fixtures and hooks
│   ├── test_smoke.py         # Smoke tests
│   └── test_regression.py    # Regression tests
│
├── utils/                     # Utilities and helpers
│   ├── config_reader.py      # Configuration management
│   ├── logger.py             # Custom logging
│   ├── test_data.py          # Test data management
│   └── helpers.py            # Helper functions
│
├── test_data/                # Test data files
│   ├── test_users.json
│   └── test_scenarios.yaml
│
├── reports/                  # Test reports (auto-generated)
├── logs/                     # Log files (auto-generated)
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables
```

## ✨ Features

- **Page Object Model (POM)**: Clean separation of test logic and page elements
- **Pytest Framework**: Powerful testing with fixtures and parametrization
- **Multi-Browser Support**: Chrome, Firefox, Safari, Edge
- **Parallel Execution**: Run tests in parallel with pytest-xdist
- **Smart Waits**: Auto-waiting for elements with custom timeout handling
- **Comprehensive Reporting**: Allure reports, HTML reports, screenshots, videos
- **CI/CD Ready**: GitHub Actions workflow included
- **Data-Driven Testing**: JSON, YAML, Excel support
- **Logging**: Detailed logging for debugging
- **Rerun Failed Tests**: Automatic retry on failures
- **Type Hints**: Full type annotation for better IDE support

## 🚀 Setup

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd "SDET playwright python"
```

2. **Create virtual environment**
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
playwright install
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your configuration
```

## 🧪 Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_smoke.py
```

### Run with specific markers
```bash
pytest -m smoke           # Smoke tests only
pytest -m regression      # Regression tests only
pytest -m critical        # Critical tests only
```

### Run in parallel
```bash
pytest -n 4              # Run with 4 workers
pytest -n auto           # Auto-detect number of CPUs
```

### Run with specific browser
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

### Run in headed mode
```bash
pytest --headed
```

### Generate Allure report
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

## 📊 Reports

### HTML Report
After test execution, find the report at:
```
reports/html/report.html
```

### Allure Report
Generate and view Allure report:
```bash
allure serve reports/allure-results
```

### Logs
Detailed logs are available at:
```
logs/test_execution.log
```

## 🔧 Configuration

### pytest.ini
Configure pytest behavior, markers, and logging.

### .env
Set environment-specific variables:
- `BASE_URL`: Application URL
- `BROWSER`: Default browser (chromium/firefox/webkit)
- `HEADLESS`: Run in headless mode (true/false)
- `DEFAULT_TIMEOUT`: Default timeout in milliseconds

## 📝 Writing Tests

### Example Test
```python
import pytest
from pages.automation_page import AutomationPage

@pytest.mark.smoke
def test_example(page):
    automation_page = AutomationPage(page)
    automation_page.navigate()
    automation_page.verify_page_loaded()
```

## 🎯 Best Practices

1. **One assertion per test method** (when possible)
2. **Use descriptive test names**
3. **Keep tests independent**
4. **Use Page Object Model**
5. **Implement proper waits**
6. **Clean test data after execution**
7. **Use markers for test organization**
8. **Maintain test data separately**

## 🔄 CI/CD Integration

GitHub Actions workflow is included in `.github/workflows/test.yml`

Push to repository to trigger automated tests on:
- Push to main/develop branches
- Pull requests
- Scheduled runs (nightly)

## 📞 Support

For issues and questions, please create an issue in the repository.

## 📄 License

MIT License
