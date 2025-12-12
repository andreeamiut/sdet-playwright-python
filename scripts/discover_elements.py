"""Script to discover actual page elements."""
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://ultimateqa.com/automation", wait_until="networkidle")
    page.wait_for_timeout(2000)
    
    print("=== Page Investigation ===\n")
    print(f"Page Title: {page.title()}\n")
    print(f"Page URL: {page.url}\n")
    
    # Check what's visible
    visible_elements = {
        "headings": [],
        "links": [],
        "buttons": [],
        "inputs": [],
        "forms": []
    }
    
    # Get headings
    h_tags = ["h1", "h2", "h3"]
    for tag in h_tags:
        elements = page.locator(tag).all()
        for elem in elements:
            if elem.is_visible():
                visible_elements["headings"].append(f"{tag}: {elem.text_content().strip()[:100]}")
    
    # Get links
    links = page.locator("a").all()
    for i, link in enumerate(links[:30]):  # First 30 links
        if link.is_visible():
            text = link.text_content().strip()[:50]
            href = link.get_attribute("href") or ""
            if text:
                visible_elements["links"].append(f"{text} -> {href[:50]}")
    
    # Get buttons
    buttons = page.locator("button, input[type='submit'], input[type='button']").all()
    for btn in buttons:
        if btn.is_visible():
            text = btn.text_content() or btn.get_attribute("value") or ""
            visible_elements["buttons"].append(f"Button: {text.strip()[:50]}")
    
    # Get inputs
    inputs = page.locator("input[type='text'], input[type='email'], textarea").all()
    for inp in inputs:
        if inp.is_visible():
            placeholder = inp.get_attribute("placeholder") or ""
            name = inp.get_attribute("name") or ""
            visible_elements["inputs"].append(f"Input: name='{name}', placeholder='{placeholder}'")
    
    # Get forms
    forms = page.locator("form").all()
    visible_elements["forms"].append(f"Found {len(forms)} forms")
    
    # Print results
    for category, items in visible_elements.items():
        print(f"\n=== {category.upper()} ({len(items)}) ===")
        for item in items[:20]:  # First 20 of each
            print(f"  - {item}")
    
    # Save to JSON
    with open("page_elements.json", "w", encoding="utf-8") as f:
        json.dump(visible_elements, f, indent=2, ensure_ascii=False)
    
    print("\n\nFull results saved to page_elements.json")
    print("\nPress Ctrl+C in terminal to close browser...")
    page.wait_for_timeout(60000)  # Wait 60 seconds
    browser.close()
