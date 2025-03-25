from behave import given, when, then


def login(username, password):
    correct_username = "test"
    correct_password = "letmein"
    return username == correct_username and password == correct_password


@given(u'användare befinner sig på inloggningssidan')
def step_given_login_page(context):
    context.page = "login_page"
    print("Användaren är på inloggnings sidan")


@when(u'användaren anger sitt användarnamn och lösenord')
def step_when_username_and_password(context):
    context.username = "test"
    context.password = "letmein"
    context.login_result = login(context.username, context.password)
    print("Användaren angav rätt användarnamn och lösenord")


@when(u'klickar på logga in knappen')
def step_when_click_login(context):
    context.button = True
    print("Tycker på inloggningsknappen")


@then(u'blir användaren inloggad och kan se sitt konto')
def step_then_user_is_logged_in(context):
    assert context.login_result is True, "Inloggning misslyckades"
    print("Inloggning OK")

# Repetition of previous login test but with wrong info
@when(u'användaren anger felaktigt användarnamn och lösenord')
def step_when_wrong_user_password(context):
    context.username = "joe"
    context.password = "letmein"
    context.login_result = login(context.username, context.password)
    print("Användaren angav fel användarnamn och lösenord")


@then(u'visa ett felmeddelande om användarnamn och lösenord')
def step_then_user_is__not_logged_in(context):
    assert context.login_result is False, "Inloggning lyckades trots felaktiga uppgifter"
    print("Inloggning NOK")

# Repetition pf previous login test but with no info
@when(u'användaren inte skriver in något alls')
def step_when_no_user_password(context):
    context.username = ""
    context.password = ""
    context.login_result = login(context.username, context.password)
    print("Användaren angav inget användarnamn och lösenord")

@when(u'användaren anger {username} och {password}')
def step_when_user_name_and_password(context, username, password):
    context.login_result = login(username, password)
    print("Testar {username} och {password}")
