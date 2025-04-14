from behave import given, when, then
from pages.start_page import StartPage
from playwright.sync_api import expect

import re

@given(u'player is on on the startpage')
def step_given__player_on_startpage(context):
    context.page.goto(context.base_url)
    context.start_page = StartPage(context.page)


@when(u'player clicks on the button "Lägg till spelare"')
def step_when__click_button_to_add_player(context):
    button = context.page.get_by_role("button").get_by_text("Lägg till spelare")
    button.click(timeout=200)


@when(u'player adds the name "{player_name}" in the inputfield')
def step_when__player_adds_name_to_input(context, player_name):
    context.start_page.fill_player_name(player_name)


@then(u'"{player_name}" shows up on the pages with the text "0:00.0"')
def step_then__player_name_shows_up(context, player_name):
    #context.page.get_by_text(re.compile("David/s+0:00:0"))
    expect(context.start_page.player_visible(player_name)).to_be_visible()
