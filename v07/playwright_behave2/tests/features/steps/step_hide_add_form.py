from behave import given, when, then
from pages.start_page import StartPage
from playwright.sync_api import expect

import re


@then(u'the form for adding a player is shown')
def step_then__form_for_adding_player_name_is_shown(context):
    expect(context.start_page.label_to_add_player()).to_be_visible(timeout=200)
    expect(context.start_page.button_to_add_player()).to_be_visible(timeout=200)
    #expect(context.start_page.input_to_add_player()).to_be_visible()


@then(u'player clicks on "Dölj" button')
def step_then_player_clicks_hide_form(context):
    context.start_page.form_click_hide()


@then(u'the form to add a player should not be shown')
def step_then__form_for_adding_player_name_is_not_shown(context):
    expect(context.start_page.label_to_add_player()).not_to_be_visible(timeout=200)
    expect(context.start_page.button_to_add_player()).not_to_be_visible(timeout=200)

