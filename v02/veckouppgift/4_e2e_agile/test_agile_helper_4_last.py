"""
Playwright pytest on https://lejonmanen.github.io/agile-helper/
Part 4: This is the "Last" page in the webapplication
For user stories and scenario see seperate document
"""

import re
from playwright.sync_api import Page, expect


# 4.1: Kommer jag åt "Last"
def test_agile_helper__last_access(page: Page):
    """
    Can I access the "Last" page
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("Last")).click(timeout=200)
    
    last_buttons = page.get_by_role("button")
    
    # Number of buttons on the middle page
    expect(last_buttons).to_have_count(4, timeout=200)
    
    # Verfiy the existance of the named buttons
    expect(last_buttons.get_by_text(re.compile("Start over"))).to_be_visible(timeout=200)
    expect(last_buttons.get_by_text(re.compile("Start every day with Daily standup"))).to_be_visible(timeout=200)
    expect(last_buttons.get_by_text(re.compile("Present your work to the product owner during Sprint review"))).to_be_visible(timeout=200)
    expect(last_buttons.get_by_text(re.compile("End the sprint by evaluating your work in Sprint retrospective"))).to_be_visible(timeout=200)
    
    
# 4.2: Kommer jag åt "Last / Daily standup"
def test_agile_helper__last_access_daily_standup(page: Page):
    """
    Can I access "Daily standup" under "Last"
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("Last")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("Start every day with Daily standup")).click(timeout=200)

    # Verify the title of "Daily standup"
    last_daily_standup_heading = page.get_by_role("heading").get_by_text(re.compile("Daily standup"))
    expect(last_daily_standup_heading).to_be_visible(timeout=200)
    

# 4.3: Kan jag använda timern på "Last / Daily standup"
#def test_agile_helper__last_daily_standup_timer(page: Page):
#    """
#    Can I use the "Daily standup" timer under "Somewhere in the middle"
#    """
#    page.goto("https://lejonmanen.github.io/agile-helper/")
#    page.get_by_role("button").get_by_text(re.compile("Last")).click(timeout=200)
#    page.get_by_role("button").get_by_text(re.compile("Start every day with Daily standup")).click(timeout=200)
#    
#    # Click to start the timer
#   page.get_by_role("button").get_by_text(re.compile("Start the standup: 10 minutes")).click(timeout=200)
#    

# 4.4: Kan jag göra "Last / Present your work to the product owner during Sprint review"
def test_agile_helper__last_sprint_review(page: Page):
    """
    Can I access "Sprint review" under "Last"
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("Last")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("Present your work to the product owner during Sprint review")).click(timeout=200)
    
    # Verify the title of "Sprint review"
    last_sprint_review_heading = page.get_by_role("heading").get_by_text(re.compile("Sprint review"))
    expect(last_sprint_review_heading).to_be_visible(timeout=200)
    

# 4.5: Kan jag göra "Last / End the sprint by evaluating your work in Sprint retrospective"
def test_agile_helper__last_sprint_retrospective(page: Page):
    """
    Can I access "Sprint retrospective" under "Last"
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("Last")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("End the sprint by evaluating your work in Sprint retrospective")).click(timeout=200)
    
    # Verify the title of "Sprint retrospective"
    last_sprint_retrospective_heading = page.get_by_role("heading").get_by_text(re.compile("Sprint retrospective"))
    expect(last_sprint_retrospective_heading).to_be_visible(timeout=200)


# 4.6: Kan jag gå tillbaka till "Start" från "Last"
def test_agile_helper__last_return_start(page: Page):
    """
    Can I return to "Start" from "Last"
    This goes trough every sub menu on the page before it returns to "Start"
    """
    page.goto("https://lejonmanen.github.io/agile-helper/")
    page.get_by_role("button").get_by_text(re.compile("Last")).click(timeout=200)
    
    # Last Daily standup
    page.get_by_role("button").get_by_text(re.compile("Start every day with Daily standup")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("Ok we're done!")).click(timeout=200)
    
    # Last Sprint review
    page.get_by_role("button").get_by_text(re.compile("Present your work to the product owner during Sprint review")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("Ok we're done. Onwards to retrospective!")).click(timeout=200)
    
    # Last Sprint retrospective
    page.get_by_role("button").get_by_text(re.compile("End the sprint by evaluating your work in Sprint retrospective")).click(timeout=200)
    page.get_by_role("button").get_by_text(re.compile("The sprint is complete")).click(timeout=200)
    
    # Back to start
    page.get_by_role("button").get_by_text(re.compile("Start over")).click(timeout=200)
    
    start_paragraph = page.get_by_role("paragraph").get_by_text(re.compile("What day of the sprint is it?"))
    expect(start_paragraph).to_be_visible(timeout=200)