from behave import given, when, then

from user import User


@given(u'that the login page can be accessed')
def step_given_page_accessable(context):
    context.user = User()


@when(u'the user submits login credentials')
def step_when__user_login(context):
    
    # The variables comes in from the 'context.table' as a row
    # They also comes in as strings any you need to convert them if needed
    
    for row in context.table:
        
        if bool(int(row["valid"])):
            assert context.user.login(str(row["username"]), str(row["password"])) is True, "Login is NOT possible when it should be possible"
        
        else:
            assert context.user.login(str(row["username"]), str(row["password"])) is False, "Login is possible when it should NOT be possible"
        


@when(u'the user submits login credentials {username} and {password}')
def step_when__user_submits_credentials(context, username, password):
    
    # The variables comes in as parameters to the function
    # By defaul they comes in as strings to the decorator but the type can be changed at this state
    
    # The extra code below is to be able to handle empry strings
    
    context.user.credential = []
    
    # Function to set empty strings as None and slice of the ends of the others
    def parse_login_string(v):
        if v == '""':
            return None
        else:
            return v[1:-1]
    
    _username = parse_login_string(username)
    _password = parse_login_string(password)
    
    if _username == None:
        context.user.credential.append("")
        
    else:
        context.user.credential.append(_username)
        
    if _password == None:
        context.user.credential.append("")
        
    else:
        context.user.credential.append(_password)
    
    
@then(u'the login is checked if it is {valid:d}')
def step_then__credentials_are_validated(context, valid):
    
    if bool(valid):
        assert context.user.login(context.user.credential[0], context.user.credential[1]) is True, "Login is NOT possible when it should be possible"
        
    else:
        assert context.user.login(context.user.credential[0], context.user.credential[1]) is False, "Login is possible when it should NOT be possible"

