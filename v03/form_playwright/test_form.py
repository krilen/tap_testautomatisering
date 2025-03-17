from playwright.sync_api import Page, expect

import re

def test_name_field(page: Page):

	page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")

	name_field = page.get_by_role("textbox").first
	expect(name_field).to_have_value(re.complie(".+"))
	 
	error_message = "Skriv in ditt namn."
	maybe_error = page.get_by_text(error_message)
	expect(maybe_error).to_be_hidden()
	 
	name_field.fill("")
	 
	expect(maybe_error).to_be_visable()

 
def test_submit_button(page: Page):
	page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")
	button = page.get_by_role("button").last
	expect(button).to_be_disabled(timeout=100)
	
	password_field = page.get_by_role("textbox").nth(3)
	password_field.fill("nfjjf232256#")
	
	expect(button).to_be_enabled(timeout=100)
	