"""
Playwright pytest on https://lejonmanen.github.io/agile-helper/
Part 2: This is the "First" page in the webapplication
For user stories and scenario see seperate document
"""

import re
from playwright.sync_api import Page, expect


# 2.1: Kommer jag åt "First"
def test_agile_helper__first_access(page: Page):
    """
    Can I access the "First" page
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("First")).click(timeout=200)
    
    first_buttons = page.get_by_role("button")
    
    # Number of buttons on the first page
    expect(first_buttons).to_have_count(3, timeout=200)
    
    # Verfiy the existance of the named buttons
    expect(first_buttons.get_by_text(re.compile("Start over"))).to_be_visible(timeout=200)
    expect(first_buttons.get_by_text(re.compile("Start off the sprint with Sprint planning"))).to_be_visible(timeout=200)
    expect(first_buttons.get_by_text(re.compile("Start every day with Daily standup"))).to_be_visible(timeout=200)


# 2.2: Kommer jag åt "First / Start off the sprint with Sprint planning"
def test_agile_helper__first_access_sprint_planning(page: Page):
    """
    Can I access "Sprint planning" under "First"
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("First")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("Start off the sprint with Sprint planning")).click(timeout=200)
    
    # Verify the title of "Sprint planning"
    first_sprint_planning_heading = page.get_by_role("heading").get_by_text(re.compile("Sprint planning"))
    expect(first_sprint_planning_heading).to_be_visible(timeout=200)
    
    
# 2.3: Kommer jag åt "First / Daily standup"
def test_agile_helper__first_access_daily_standup(page: Page):
    """
    Can I access "Daily standup" under "First"
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("First")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("Start every day with Daily standup")).click(timeout=200)

    # Verify the title of "Dailt standup"
    first_daily_standup_heading = page.get_by_role("heading").get_by_text(re.compile("Daily standup"))
    expect(first_daily_standup_heading).to_be_visible(timeout=200)
    
    
# 2.4: Kan jag använda timern på "First / Daily standup"
#def test_agile_helper__first_daily_standup_timer(page: Page):
#    """
#    Can I use the "Daily standup" timer under "First"
#    """
#    page.goto("https://lejonmanen.github.io/agile-helper/")
#    page.get_by_role("button").get_by_text(re.compile("First")).click(timeout=200)
#    page.get_by_role("button").get_by_text(re.compile("Start every day with Daily standup")).click(timeout=200)
#    
#    # Click to start the timer
#   page.get_by_role("button").get_by_text(re.compile("Start the standup: 10 minutes")).click(timeout=200)
#    
 
 
# 2.5: Kan jag gå tillbaka till "Start" från "First"
def test_agile_helper__first_return_start(page: Page):
    """
    Can I return to "Start" from "First"
    This goes trough every sub menu on the page before it returns to "Start"
    """
    
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("First")).click(timeout=200)
    
    # Sprint planning
    page.get_by_role("button").get_by_text(re.compile("Start off the sprint with Sprint planning")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("Ok we're done. Start the sprint!")).click(timeout=200)
    
    # First Daily standup
    page.get_by_role("button").get_by_text(re.compile("Start every day with Daily standup")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("Ok we're done!")).click(timeout=200)
    
    # Back to start
    page.get_by_role("button").get_by_text(re.compile("Start over")).click(timeout=200)
    
    start_paragraph = page.get_by_role("paragraph").get_by_text(re.compile("What day of the sprint is it?"))
    expect(start_paragraph).to_be_visible(timeout=200)