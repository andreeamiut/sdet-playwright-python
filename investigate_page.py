"""Quick script to investigate the page structure."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://ultimateqa.com/automation")
    page.wait_for_load_state("networkidle")
    
    print("\n=== Looking for form elements ===")
    
    # Check for input fields
    inputs = page.locator("input[type='text']").all()
    print(f"\nFound {len(inputs)} text inputs")
    for i, inp in enumerate(inputs):
        name = inp.get_attribute("name") or "no-name"
        placeholder = inp.get_attribute("placeholder") or "no-placeholder"
        id_attr = inp.get_attribute("id") or "no-id"
        print(f"  Input {i+1}: name='{name}', placeholder='{placeholder}', id='{id_attr}'")
    
    # Check for textareas
    textareas = page.locator("textarea").all()
    print(f"\nFound {len(textareas)} textareas")
    for i, ta in enumerate(textareas):
        name = ta.get_attribute("name") or "no-name"
        placeholder = ta.get_attribute("placeholder") or "no-placeholder"
        id_attr = ta.get_attribute("id") or "no-id"
        print(f"  Textarea {i+1}: name='{name}', placeholder='{placeholder}', id='{id_attr}'")
    
    # Check for submit buttons
    buttons = page.locator("button, input[type='submit']").all()
    print(f"\nFound {len(buttons)} buttons/submit inputs")
    for i, btn in enumerate(buttons):
        name = btn.get_attribute("name") or "no-name"
        btn_type = btn.get_attribute("type") or "no-type"
        text = btn.text_content() or "no-text"
        class_attr = btn.get_attribute("class") or "no-class"
        print(f"  Button {i+1}: name='{name}', type='{btn_type}', text='{text.strip()}', class='{class_attr}'")
    
    # Check for links
    links = page.locator("a[href*='page'], a[href*='landing'], a[href*='pricing']").all()
    print(f"\nFound {len(links)} relevant links")
    for i, link in enumerate(links):
        href = link.get_attribute("href") or "no-href"
        text = link.text_content() or "no-text"
        print(f"  Link {i+1}: href='{href}', text='{text.strip()}'")
    
    input("\n\nPress Enter to close browser...")
    browser.close()
