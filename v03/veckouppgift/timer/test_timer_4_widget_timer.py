from playwright.sync_api import Page, expect

import re

# TS04
def test_timer__modify_timer_time(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    # Add timer widget
    page.get_by_role("button").get_by_text(re.compile("timer", re.IGNORECASE)).click(timeout=200)

    # Verify the standard time
    timer = page.locator(".widget").nth(1)
    timer_time_before = timer.locator(".row.time").get_by_text(re.compile("15:00", re.IGNORECASE))
    expect(timer_time_before).to_be_visible(timeout=200)
    
    # Change the time
    timer.locator(".icon.settings").click(timeout=200)
    timer_input = timer.get_by_role("textbox")
    timer_input.fill("1")
    
    timer.get_by_role("button").nth(1).click(timeout=200)
    
    # Verify the changed time
    timer_time_after = timer.locator(".row.time").get_by_text(re.compile("1:00", re.IGNORECASE))
    expect(timer_time_after).to_be_visible(timeout=200)
    
    # Verify that there is still one widged on the webpage
    expect(page.locator(".widget")).to_have_count(2, timeout=200) 


# TS05
def test_timer__verify_timer_works(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")
    
    # Add timer widget
    page.get_by_role("button").get_by_text(re.compile("timer", re.IGNORECASE)).click(timeout=200)

    # Verify the standard time
    timer = page.locator(".widget").nth(1)
    timer_time_before = timer.locator(".row.time").get_by_text(re.compile("15:00", re.IGNORECASE))
    expect(timer_time_before).to_be_visible(timeout=200)
    
    # Start the timer, wait, stop the timer
    timer.get_by_role("button").nth(0).click(timeout=200) 
    page.wait_for_timeout(5000) # Wait for 5 sec
    timer.get_by_role("button").nth(0).click(timeout=200)
    
    # Verify that the timer has changed
    timer_time_after = timer.locator(".row.time").get_by_text(re.compile("^14+", re.IGNORECASE))
    expect(timer_time_after).to_be_visible(timeout=200)
    
    # Reset the timer and verify
    timer.get_by_role("button").nth(1).click(timeout=200)
    
    timer_time_reset = timer.locator(".row.time").get_by_text(re.compile("15:00", re.IGNORECASE))
    expect(timer_time_reset).to_be_visible(timeout=200)