from playwright.sync_api import Page, expect

import re


# TS06
def test_timer__change_text(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # Add notes
    page.get_by_role("button").get_by_text(re.compile("note", re.IGNORECASE)).click(timeout=200)

    notes = page.locator(".widget").nth(1)

    # Check that the default text is present in the new notes
    notes_text = notes.get_by_role("textbox").get_by_text("Click to change text")
    expect(notes_text).to_be_hidden()
    
    # Using JS to show the input field
    notes.evaluate("""
        const inputElement = document.querySelector('input[placeholder="Description"]');
        if (inputElement) {
            inputElement.style.display = 'inline';
        }
    """)

    # Set a new text in the input field
    _new_text = "Test text"
    notes.get_by_placeholder("Description").fill(_new_text)

    # Using JS to hide the input field
    notes.evaluate("""
        const inputElement = document.querySelector('input[placeholder="Description"]');
        if (inputElement) {
            inputElement.style.display = 'none';
        }
    """)
    
    # Verify that the input filed with the new text is hidden
    notes_text = notes.get_by_role("textbox").get_by_text(_new_text)
    expect(notes_text).to_be_hidden()
    
    # Verify that there is still one widged on the webpage
    expect(page.locator(".widget")).to_have_count(2, timeout=200) 
