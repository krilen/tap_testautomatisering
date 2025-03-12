"""
Playwright pytest on https://lejonmanen.github.io/agile-helper/
Part 3: This is the "Somewhere in the middle" page in the webapplication
For user stories and scenario see seperate document
"""

import re
from playwright.sync_api import Page, expect


# 3.1: Kommer jag åt "Somewhere in the middle"
def test_agile_helper__middle_access(page: Page):
    """
    Can I access the "Somewhere in the middle" page
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("Somewhere in the middle")).click(timeout=200)
    
    middle_buttons = page.get_by_role("button")
    
    # Number of buttons on the middle page
    expect(middle_buttons).to_have_count(2, timeout=200)
    
    # Verfiy the existance of the named buttons
    expect(middle_buttons.get_by_text(re.compile("Start over"))).to_be_visible(timeout=200)
    expect(middle_buttons.get_by_text(re.compile("Start every day with Daily standup"))).to_be_visible(timeout=200)
    

# 3.2: Kommer jag åt "Somewhere in the middle / Daily standup"
def test_agile_helper__middle_access_daily_standup(page: Page):
    """
    Can I access "Daily standup" under "Somewhere in the middle"
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("Somewhere in the middle")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("Start every day with Daily standup")).click(timeout=200)

    # Verify the title of "Daily standup"
    middle_daily_standup_heading = page.get_by_role("heading").get_by_text(re.compile("Daily standup"))
    expect(middle_daily_standup_heading).to_be_visible(timeout=200)
    

# 3.3: Kan jag använda timern på "Somewhere in the middle / Daily standup"
#def test_agile_helper__middle_daily_standup_timer(page: Page):
#    """
#    Can I use the "Daily standup" timer under "Somewhere in the middle"
#    """
#    page.goto("https://lejonmanen.github.io/agile-helper/")
#    page.get_by_role("button").get_by_text(re.compile("Somewhere in the middle")).click(timeout=200)
#    page.get_by_role("button").get_by_text(re.compile("Start every day with Daily standup")).click(timeout=200)
#    
#    # Click to start the timer
#   page.get_by_role("button").get_by_text(re.compile("Start the standup: 10 minutes")).click(timeout=200)
#    

# 3.4: Kan jag gå tillbaka till "Start" från "Somewhere in the middle"
def test_agile_helper__middle_return_start(page: Page):
    """
    Can I return to "Start" from "Somewhere in the middle"
    This goes trough every sub menu on the page before it returns to "Start"
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("Somewhere in the middle")).click(timeout=200)
    
    # Middle Daily standup
    page.get_by_role("button").get_by_text(re.compile("Start every day with Daily standup")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("Ok we're done!")).click(timeout=200)
    
    # Back to start
    page.get_by_role("button").get_by_text(re.compile("Start over")).click(timeout=200)
    
    start_paragraph = page.get_by_role("paragraph").get_by_text(re.compile("What day of the sprint is it?"))
    expect(start_paragraph).to_be_visible(timeout=200)