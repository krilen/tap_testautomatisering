"""
Playwright pytest on https://lejonmanen.github.io/agile-helper/
Part 1: This is start webpage in the webapplication
For user stories and scenario see seperate document

"""

import re
from playwright.sync_api import Page, expect


# 1.1: Kommer jag åt webbsidan
def test_agile_helper__start_general_access(page: Page):
    """
    Do I have access to the start page at all
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    
    start_heading = page.get_by_role("heading").get_by_text("Agile helper")
    expect(start_heading).to_be_visible(timeout=200)
    
    
# 1.2: Kan jag se knappar på webbsidan
def test_agile_helper__start_verify_buttons(page: Page):
    """
    Can I see the 3 buttons on the start page
    and does their defined name exists
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    
    start_buttons = page.get_by_role("button")
    
    # Number of buttons on the start page
    expect(start_buttons).to_have_count(3, timeout=200)
    
    # Verfiy the existance of the named buttons
    expect(start_buttons.get_by_text(re.compile("First"))).to_be_visible(timeout=200)
    expect(start_buttons.get_by_text(re.compile("Somewhere in the middle"))).to_be_visible(timeout=200)
    expect(start_buttons.get_by_text(re.compile("Last"))).to_be_visible(timeout=200)
    