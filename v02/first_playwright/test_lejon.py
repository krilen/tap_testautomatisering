import re
from playwright.sync_api import Page, expect

def test_basic__webpage_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")
    
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))
    
    
def test_daily_standup__nav_to_daily_standup(page):
    # Webpage
    page.goto("https://lejonmanen.github.io/agile-helper/")
    
    # Hitta en knapp, button, som har texten "Somewhere in the middle", klicka på den
    locator_1 = page.get_by_role("button")
    button_1 = locator_1.get_by_text(re.compile("Somewhere in the middle"))
    button_1.click(timeout=100)
    
    # Hitta en knapp, button, som har texten "Daily standup"
    # Det skall bara finnas en knapp som uppfyller detta, klicka på den
    button_2 = page.get_by_role("button").get_by_text(re.compile("Daily standup"))
    expect(button_2).to_have_count(1, timeout=100) # locator assertion
    button_2.click(timeout=100)
    
    # Hitta en rubrik som har texten "Daily standup"
    heading = page.get_by_role("heading").get_by_text(re.compile("Daily standup"))
    expect(heading).to_be_visible(timeout=100)