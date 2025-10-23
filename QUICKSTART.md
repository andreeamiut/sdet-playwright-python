# Quick Start Guide

## Installation & Setup

### Method 1: Automated Setup (Recommended)

**Windows:**
```powershell
.\setup.bat
```

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

### Method 2: Manual Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Install Playwright browsers:**
```bash
playwright install
```

3. **Create .env file:**
```bash
cp .env.example .env
```

4. **Edit .env with your settings**

## Running Tests

### Quick Commands

```bash
# Run all smoke tests
pytest -m smoke

# Run all regression tests
pytest -m regression

# Run all tests
pytest

# Run in parallel (4 workers)
pytest -n 4

# Run with specific browser
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit

# Run in headed mode
pytest --headed

# Run specific test file
pytest tests/test_smoke.py

# Run specific test
pytest tests/test_smoke.py::TestSmoke::test_page_loads_successfully
```

### Using the test runner script

```bash
# Run smoke tests
python run_tests.py smoke

# Run regression tests
python run_tests.py regression

# Run all tests
python run_tests.py all

# Run in parallel
python run_tests.py parallel

# Generate Allure report
python run_tests.py report
```

## Viewing Reports

### HTML Report
After running tests, open:
```
reports/html/report.html
```

### Allure Report
```bash
# Generate and view Allure report
allure serve reports/allure-results
```

## Framework Structure

```
📦 SDET playwright python
├─ 📁 pages/                  # Page Object Models
│  ├─ base_page.py           # Base page class
│  └─ automation_page.py     # Ultimate QA page
│
├─ 📁 tests/                  # Test cases
│  ├─ conftest.py            # Pytest fixtures
│  ├─ test_smoke.py          # Smoke tests
│  └─ test_regression.py     # Regression tests
│
├─ 📁 utils/                  # Utilities
│  ├─ logger.py              # Logging
│  ├─ config_reader.py       # Configuration
│  ├─ test_data.py           # Test data
│  └─ helpers.py             # Helper functions
│
├─ 📁 test_data/              # Test data files
│  ├─ test_users.json
│  └─ test_scenarios.yaml
│
├─ 📁 .github/workflows/      # CI/CD
│  └─ test.yml               # GitHub Actions
│
├─ 📄 pytest.ini              # Pytest config
├─ 📄 requirements.txt        # Dependencies
├─ 📄 .env                    # Environment vars
└─ 📄 README.md              # Documentation
```

## Key Features

✅ **Page Object Model** - Clean, maintainable code structure  
✅ **Pytest Framework** - Powerful testing with fixtures  
✅ **Multi-Browser Support** - Chromium, Firefox, WebKit  
✅ **Parallel Execution** - Run tests faster  
✅ **Smart Waits** - Auto-waiting for elements  
✅ **Rich Reporting** - Allure + HTML reports  
✅ **Screenshots/Videos** - Captured on failure  
✅ **CI/CD Ready** - GitHub Actions included  
✅ **Type Hints** - Better IDE support  
✅ **Logging** - Comprehensive logging system  

## Test Markers

```python
@pytest.mark.smoke       # Quick smoke tests
@pytest.mark.regression  # Full regression suite
@pytest.mark.critical    # Critical path tests
@pytest.mark.ui          # UI tests
@pytest.mark.slow        # Slower tests
```

## Configuration (.env)

```ini
BASE_URL=https://ultimateqa.com/automation
BROWSER=chromium
HEADLESS=false
DEFAULT_TIMEOUT=30000
SCREENSHOT_ON_FAILURE=true
VIDEO_ON_FAILURE=true
TRACE_ON_FAILURE=true
MAX_WORKERS=4
```

## Troubleshooting

### Playwright not installed
```bash
playwright install
```

### Missing dependencies
```bash
pip install -r requirements.txt
```

### Permission denied (Linux/Mac)
```bash
chmod +x setup.sh
```

## Best Practices

1. ✅ Keep tests independent
2. ✅ Use descriptive test names
3. ✅ One assertion per test (when possible)
4. ✅ Use Page Object Model
5. ✅ Implement proper waits
6. ✅ Clean test data after execution
7. ✅ Use markers for organization
8. ✅ Maintain test data separately

## Contributing

1. Create feature branch
2. Write tests
3. Ensure all tests pass
4. Submit pull request

## Support

For issues, check:
- README.md
- Test logs in `logs/`
- Screenshots in `screenshots/`
- Traces in `traces/`
