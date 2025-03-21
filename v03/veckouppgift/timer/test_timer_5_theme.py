from playwright.sync_api import Page, expect

import re

# TS07
def test_timer__theme(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    possible_themes = [("Light", ""), ("Dark", "dark"), ("Forest", "forest"), ("Orange", "orange")]

    # Verify buttons that will NOT add a widget
    theme_buttons = page.get_by_role("button").get_by_text(re.compile("^((?!add).)*$", re.IGNORECASE)) # Contains not "add"
    expect(theme_buttons).to_have_count(len(possible_themes), timeout=200)

    # Check each defined theme button
    for theme_button in possible_themes:
        button = page.get_by_role("button").get_by_text(re.compile(theme_button[0], re.IGNORECASE))

        button.click(timeout=200)

        # Verify the html 'data-theme' when the button is clicked
        expect(page.locator("//html")).to_have_attribute("data-theme", theme_button[1])

        # Verify that the button gets selected
        expect(button).to_have_class("ghost selected")


