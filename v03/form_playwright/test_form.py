import re
from playwright.sync_api import Page, expect


def test_name_field(page: Page):

	page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")

	# Find first field and make sure it is not empty
	name_field = page.get_by_role("textbox").first
	expect(name_field).to_have_value(re.compile(".+"))
	
	# Kontrollera om hjälptext är dold
	error_message = "Skriv in ditt namn."
	maybe_error = page.get_by_text(error_message)
	expect(maybe_error).to_be_hidden()
	 
	# Fyller fältet med inget, tom sträng
	name_field.fill("")
	
	# Fältet skall nu dyka upp
	expect(maybe_error).to_be_visible()


def test_submit_button(page: Page):
	page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")
 
	# Submit knappen
	button = page.get_by_role("button").last
	
	# Submit knappen skall var inaktiverad från start
	expect(button).to_be_disabled(timeout=100)
	
	# Fyll i lösenords fältet med ett bra lösen
	password_field = page.get_by_role("textbox").nth(3)
	password_field.fill("nfjjf232256#")

	# Submit knappen skall var aktiv när allt har fyllts i
	expect(button).to_be_enabled(timeout=100)
	