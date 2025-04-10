from behave import given, when, then
from playwright.sync_api import expect

from pages.friend import Friend




@given(u'access to the add webpage')
def step_given__access_to_friend_add_page(context):
    context.friend = Friend(context.page)
    context.page.goto(context.friend.url_add)


@then(u'I can verify that I am on the add page')
def step__verify_the_add_page_is_shown(context):
    expect(context.friend.verify_add_page).to_be_disabled(timeout=200)


@when(u'I add a friend')
def step_when__add_friend(context):
    context.friend.add_friend("john", "doe@spam.net")


@when(u'a second friend')
def step_when__add_friend2(context):
    context.friend.add_friend("mary", "doe@spam.com")


@then(u'I can verify that I have {count:d} friend')
def step_then__verify_the_number_of_friends(context, count):
    assert context.friend.count_friends == count, "Wrong count of friends"


@when(u'adding friends: {name}, {email}')
def step_when__verify_add_friend(context, name, email):
    context.friend.verify_add = context.friend.verify_add_friend(name, email)


@then(u'I can verify if the friend should be added: {should_be_added:d}')
def step_then__verify_possible_to_add_friend(context, should_be_added):
    if bool(should_be_added):
        expect(context.friend.verify_add[0]).to_be_enabled()

    else:
        expect(context.friend.verify_add[0]).to_be_disabled()


@then(u'I can verify if a warning message should appear: {should_be_added:d}')
def step_then__verify_error_message_if_not_possible_to_add_friend(context, should_be_added):
    if bool(should_be_added):
        expect(context.friend.verify_add[1]).to_be_hidden()
        
    else:
        expect(context.friend.verify_add[1]).to_be_visible()