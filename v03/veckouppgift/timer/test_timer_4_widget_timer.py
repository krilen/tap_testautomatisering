from playwright.sync_api import Page, expect

import re

# TS01
def test_timer__access(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # Verify that no active widgets are present on the page
    widget = page.locator(".widget")
    expect(widget).to_have_count(1, timeout=100)

    # Number of "Add" buttons on the page 
    add_buttons = page.get_by_role("button").get_by_text(re.compile("add", re.IGNORECASE))
    expect(add_buttons).to_have_count(2, timeout=100)
