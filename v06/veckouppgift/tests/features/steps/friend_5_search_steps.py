from behave import given, when, then
from playwright.sync_api import expect

from pages.friend import Friend


@then(u'I can search after them')
def step_then__search_for_friends(context):
    
    context.friend = Friend(context.page)
    
    
    for row in context.table:
        
        count = int(row["count"])
        
        
        search_count = context.friend.search_friend(row["search"])
        
        print(row["search"], count, search_count)
        
        
        assert int(row["count"]) == context.friend.search_friend(row["search"]), f"The count of friend search for: '{row["search"]}' is not correct"



