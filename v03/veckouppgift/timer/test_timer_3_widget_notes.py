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
    expect(notes_text).to_be_hidden() # Text box hidden

    # Change the text
    notes.focus(timeout=200)
    #expect(notes.get_by_role("heading")).get_by_text("Click to change text")

    # Add new text and verify it
    _new_text = "Test text"
    notes_text.fill(_new_text)
    #expect(notes).to_have_value(_new_text)

    # Verify that there are 1 active widgets are present on the page
    #expect(page.locator(".widget")).to_have_count(2, timeout=200) 
