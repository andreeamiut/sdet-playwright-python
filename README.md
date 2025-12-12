# 🎭 Playwright Python Test Automation Framework

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Playwright](https://img.shields.io/badge/Playwright-Latest-45ba4b?style=flat&logo=playwright&logoColor=white)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://pytest.org)
[![CI](https://github.com/andreeamiut/sdet-playwright-python/actions/workflows/test.yml/badge.svg)](https://github.com/andreeamiut/sdet-playwright-python/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready test automation framework built with **Playwright** and **Python**, implementing industry best practices including Page Object Model, parallel execution, and CI/CD integration.

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **Page Object Model** | Clean separation of test logic and page interactions |
| **Multi-Browser** | Chromium, Firefox, WebKit support |
| **Parallel Execution** | pytest-xdist for faster test runs |
| **CI/CD Ready** | GitHub Actions workflow included |
| **Rich Reporting** | Allure reports, HTML reports, screenshots, videos |
| **Data-Driven** | JSON, YAML test data support |
| **Type Hints** | Full annotations for IDE support |

## 🏗️ Project Structure

```
sdet-playwright-python/
├── pages/                    # Page Object Models
│   ├── base_page.py         # Base class with common methods
│   └── automation_page.py   # Page-specific implementations
├── tests/                    # Test suites
│   ├── test_smoke.py        # Smoke tests
│   └── test_regression.py   # Regression tests
├── utils/                    # Utilities
│   ├── config_reader.py     # Configuration management
│   ├── logger.py            # Custom logging
│   └── helpers.py           # Helper functions
├── test_data/               # Test data files
├── .github/workflows/       # CI/CD pipelines
├── conftest.py              # Pytest fixtures
├── pytest.ini               # Pytest configuration
└── requirements.txt         # Dependencies
```

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/andreeamiut/sdet-playwright-python.git
cd sdet-playwright-python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
playwright install

# Run tests
pytest
```

## 🧪 Running Tests

```bash
# All tests
pytest

# Specific markers
pytest -m smoke
pytest -m regression

# Parallel execution
pytest -n auto

# Specific browser
pytest --browser firefox

# With Allure report
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

## ⚙️ Configuration

Environment variables (`.env`):

```env
BASE_URL=https://your-app.com
BROWSER=chromium
HEADLESS=true
DEFAULT_TIMEOUT=30000
```

## 📝 Writing Tests

```python
import pytest
from pages.automation_page import AutomationPage

@pytest.mark.smoke
def test_user_login(page):
    automation_page = AutomationPage(page)
    automation_page.navigate()
    automation_page.login("user@example.com", "password")
    assert automation_page.is_logged_in()
```

## 📊 Reports

| Report Type | Location |
|-------------|----------|
| HTML Report | `reports/html/report.html` |
| Allure Report | `reports/allure-results/` |
| Logs | `logs/test_execution.log` |

## 🔄 CI/CD

Tests run automatically on:
- Push to `main`/`develop` branches
- Pull requests
- Scheduled nightly runs

## 👤 Author

**Andreea Miut** - Senior QA Automation Engineer

[![GitHub](https://img.shields.io/badge/GitHub-andreeamiut-181717?style=flat&logo=github)](https://github.com/andreeamiut)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/andreeamiut/)

## 📄 License

This project is licensed under the MIT License.
