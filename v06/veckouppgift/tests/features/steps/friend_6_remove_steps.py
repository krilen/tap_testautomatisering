from behave import given, then
from playwright.sync_api import expect

from pages.friend import Friend

@then(u'I can remove them all')
def step_then__remove_all_friends(context):
    context.friend.remove_friends
    
    assert context.friend.count_friends == 0


@then(u'I remove a friend')
def step_then_remove_one_friend(context):
    
    friends_count_before = context.friend.count_friends
    
    context.friend.remove_friend(0)
    
    friends_count_after = context.friend.count_friends
    
    assert (friends_count_before > friends_count_after), "The number of friends did not get reduced!"