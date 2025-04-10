from behave import given, then
from playwright.sync_api import expect

from pages.friend import Friend

@given(u'access to the list webpage')
def step_given__access_to_friend_list_page(context):
    context.friend = Friend(context.page)
    context.page.goto(context.friend.url_list)


@then(u'I can verify that I am on the list page')
def step_then__verify_the_list_page_is_shown(context):
    expect(context.friend.verify_list_page).to_be_visible(timeout=200)


@then(u'I can see that there is a section for my friends to be saved')
def step_then__verify_section_for_friends(context):
    expect(context.friend.list_section).to_be_visible(timeout=200)


@then(u'I can count the number of friends')
def step_then__count_the_number_of_friends(context):
    assert context.friend.count_friends >= 0


@then(u'I can remove them all')
def step_then__remove_all_friends(context):
    context.friend.remove_friends
    
    assert context.friend.count_friends == 0


