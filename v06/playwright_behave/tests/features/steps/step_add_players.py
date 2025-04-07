from behave import when, then

@when(u'player clicks on the button "Lägg till spelare"')
def step_when__clicks_to_add_player(context):
    raise NotImplementedError(u'STEP: When player clicks on the button "Lägg till spelare"')    


@when(u'playes adds the name "David" in the inputfield')
def step_impl(context):
    raise NotImplementedError(u'STEP: When playes adds the name "David" in the inputfield')     


@then(u'"David" shows up on the pages with the text "0:00.0"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "David" shows up on the pages with the text "0:00.0"')


@when(u'playes adds the name "Goliat" in the inputfield')
def step_impl(context):
    raise NotImplementedError(u'STEP: When playes adds the name "Goliat" in the inputfield')    


@then(u'"Goliat" shows up on the pages with the text "0:00.0"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "Goliat" shows up on the pages with the text "0:00.0"')