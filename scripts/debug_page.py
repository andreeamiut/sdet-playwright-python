"""Debug script to extract page HTML."""
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://ultimateqa.com/automation")
    time.sleep(3)  # Wait for page to load
    
    # Get the HTML
    html = page.content()
    
    # Save to file
    with open("page_content.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print("Page HTML saved to page_content.html")
    print(f"Total HTML length: {len(html)} characters")
    
    # Check if elements exist
    try:
        name_field = page.locator("input[type='text']").first
        print(f"\nFirst text input found: {name_field.count()} instances")
    except Exception as e:
        print(f"\nNo text input found: {e}")
    
    browser.close()
