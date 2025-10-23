#!/bin/bash
# Setup script for Playwright Python Framework (Linux/Mac)

echo "========================================"
echo "Playwright Python Framework Setup"
echo "========================================"
echo ""

echo "Step 1: Installing Python dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo ""
echo "Step 2: Installing Playwright browsers..."
python3 -m playwright install

echo ""
echo "Step 3: Creating necessary directories..."
mkdir -p logs screenshots videos traces reports/html reports/allure-results

echo ""
echo "Step 4: Setting up environment file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo ".env file created from .env.example"
else
    echo ".env file already exists"
fi

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your configuration"
echo "2. Run smoke tests: pytest -m smoke"
echo "3. Run all tests: pytest"
echo "4. View README.md for more information"
echo ""
