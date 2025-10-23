@echo off
REM Setup script for Playwright Python Framework

echo ========================================
echo Playwright Python Framework Setup
echo ========================================
echo.

echo Step 1: Installing Python dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Step 2: Installing Playwright browsers...
python -m playwright install

echo.
echo Step 3: Creating necessary directories...
if not exist "logs" mkdir logs
if not exist "screenshots" mkdir screenshots
if not exist "videos" mkdir videos
if not exist "traces" mkdir traces
if not exist "reports" mkdir reports
if not exist "reports\html" mkdir reports\html
if not exist "reports\allure-results" mkdir reports\allure-results

echo.
echo Step 4: Setting up environment file...
if not exist ".env" (
    copy .env.example .env
    echo .env file created from .env.example
) else (
    echo .env file already exists
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file with your configuration
echo 2. Run smoke tests: pytest -m smoke
echo 3. Run all tests: pytest
echo 4. View this README.md for more information
echo.
pause
