from behave import given, when, then
from playwright.sync_api import expect

from pages.friend_start import FriendStart



@given(u'access to the webpage')
def step_given__access_to_friend_page(context):
    context.friend = FriendStart(context.page)
    context.page.goto(context.friend.url_start)


@then(u'I can see that I am on my friends page')
def step_then__i_am_on_my_friends_page(context):
    expect(context.friend.page_heading(""))