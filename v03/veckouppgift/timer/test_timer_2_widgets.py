from playwright.sync_api import Page, expect

import re

# TS02
def test_timer__add_remove_widgets(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # Verify that no active widgets are present on the page
    expect(page.locator(".widget")).to_have_count(1, timeout=200)

    # Add notes and timer widget
    page.get_by_role("button").get_by_text(re.compile("note", re.IGNORECASE)).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("timer", re.IGNORECASE)).click(timeout=200)

    # Verify that there are 2 active widgets are present on the page
    expect(page.locator(".widget")).to_have_count(3, timeout=200) 

    # Remove notes and timer widget
    widget_close = page.locator(".icon.close")
    widget_close.first.click(timeout=200)
    widget_close.first.click(timeout=200)

    # Verify that no active widgets are present on the page
    expect(page.locator(".widget")).to_have_count(1, timeout=200)


# TS03
def test_timer__change_order_widgets(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # Add notes and timer widget
    page.get_by_role("button").get_by_text(re.compile("note", re.IGNORECASE)).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("timer", re.IGNORECASE)).click(timeout=200)

    # Verify that the notes are at the top
    notes = page.locator(".widget").nth(1)
    notes_heading = notes.get_by_role("heading").get_by_text(re.compile("text", re.IGNORECASE))
    expect(notes_heading).to_be_visible(timeout=200)

    # Move the timer to top
    page.locator(".icon.up").nth(1).click(timeout=200)

    # Verify that the timer are on top
    timer = page.locator(".widget").nth(1)
    timer_heading = timer.get_by_role("heading").get_by_text(re.compile("break", re.IGNORECASE))
    expect(timer_heading).to_be_visible(timeout=200)

    # Verify that there are 2 active widgets are present on the page
    expect(page.locator(".widget")).to_have_count(3, timeout=200) 

