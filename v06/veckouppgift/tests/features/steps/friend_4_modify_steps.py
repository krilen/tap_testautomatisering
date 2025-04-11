from behave import given, when, then
from playwright.sync_api import expect

from pages.friend import Friend

import re


@then(u'I can change the friends and verify the change')
def step_then__change_a_friends_information(context):
    
    context.friend = Friend(context.page)
    context.page.goto(context.friend.url_list)
    
    for row in context.table:
        
        context.friend.modify_friend(row["change_from"], row["change_to"])
        
        if bool(int(row["valid"])):
            expect(context.page.get_by_text(re.compile(row["change_to"], re.IGNORECASE)).first).to_be_visible()
            expect(context.page.get_by_text(re.compile(row["change_from"], re.IGNORECASE)).first).not_to_be_visible()
            
        else:
            expect(context.page.get_by_text(re.compile(row["change_to"], re.IGNORECASE)).first).not_to_be_visible()
    
    
@then(u'I can verify that all information is supplied when trying to modify a friend')
def step_then__verify_change_data_friend(context):
    
    context.friend = Friend(context.page)
    context.page.goto(context.friend.url_list)

    for row in context.table:
        
        result = context.friend.verify_modify_friend(row["change_name"], row["change_email"])
        
        if bool(int(row["valid"])):
            expect(result.locator("section").get_by_role("button")).to_be_enabled()
            expect(result.locator(".error")).not_to_be_visible()
            
        else:
            expect(result.locator("section").get_by_role("button")).to_be_disabled()
            expect(result.locator(".error")).to_be_visible()
