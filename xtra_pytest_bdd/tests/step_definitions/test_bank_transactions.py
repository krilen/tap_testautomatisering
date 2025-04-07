import pytest  
from pytest_bdd import scenarios, given, when, then  
  
# Load all scenarios from the feature file  
scenarios("../features/bank_transactions.feature")  # Which scenario to use
  
# Fixtures  
@pytest.fixture  
def account_balance():  
    return {"balance": 100}  # Using a dictionary to allow modifications  
  
# Given Steps  
@given("the account balance is $100")  # from feature
def step_given__account_initial_balance(account_balance):  
    account_balance["balance"] = 100  
  
# When Steps  
@when("I deposit $20")  # from feature
def step_when__deposit(account_balance):
    account_balance["balance"] += 20  
  
# Then Steps  
@then("the account balance should be $120")  # from feature
def step_then__account_balance_should_be(account_balance):  
    assert account_balance["balance"] == 120