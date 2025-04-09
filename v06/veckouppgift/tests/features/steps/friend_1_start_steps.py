from behave import given, when, then
from playwright.sync_api import expect

from pages.friend_start import FriendStart


@given(u'access to the start webpage')
def step_given__access_to_friend_page(context):
    context.friend = FriendStart(context.page)
    context.page.goto(context.friend.url_start)


@then(u'I can see that I am on my friends page')
def step_then__on_my_friends_page(context):
    expect(context.friend.page_heading("mina vänner")).to_be_visible(timeout=200)


@then(u'I can see that there are 3 links on my friends page')
def step_then__verify_3_links(context):
    expect(context.friend.nav_links).to_have_count(3, timeout=200)


@then(u'I can see that the links have the following links')
def step_then__verify_the_link_and_linktext(context):
    
    for row in context.table:
        text, url = context.friend.nav_link(int(row["place"]), row["text"], row["url"])
        
        expect(text).to_be_visible(timeout=200)
        assert url is True, f"The link ({row["url"]}) was not correct"


@when(u'I can see that the link for the page {text} page is active')
def step_when__verify_link_for_page_is_active(context, text):
    expect(context.friend.nav_link_active(text)).to_be_visible(timeout=200)


@then(u'I can verify that I am on the start page')
def step_then__verify_the_start_page_is_shown(context):
    expect(context.friend.verify_page()).to_be_visible(timeout=200)
