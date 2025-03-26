from behave import given, when, then

from cart import Cart

@given(u'that a shopping cart is present')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given that a shopping cart is present')


@when(u'the user places the item in the shopping cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user places the item in the shopping cart')


@then(u'the user can see that the shopping cart is not empty')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user can see that the shopping cart is not empty')


@when(u'the user removes the item from the shopping cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user removes the item from the shopping cart')


@then(u'the user can see that the shopping cart is empty')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user can see that the shopping cart is empty')


@when(u'user add items to the shopping cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user add items to the shopping cart')


@then(u'the user can see the number of items and the total amount to pay for the items in the shopping cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user can see the number of items and the total amount to pay for the items in the shopping cart')


@then(u'the user can see the count of each item in the shopping cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user can see the count of each item in the shopping cart')


@when(u'chooses to delete them all at once')
def step_impl(context):
    raise NotImplementedError(u'STEP: When chooses to delete them all at once')

"""
@given(u'that a shopping cart is present')
def step_give__cart_present(context):
    context.cart = Cart()
    
    print("User has access to a shopping cart")


@when(u'the user places the item in the shopping cart')
def step_when__item_added_to_cart(context):
    context.cart.add_item("item1", 200)
    context.empty_cart = context.cart.is_empty()
    
    print("item added to shopping cart")


@then(u'the user can see that the shopping cart is not empty')
def step_then__verify_cart_not_empty(context):
    assert context.empty_cart is False, "Shopping cart is empty"


@when(u'the user removes the item from the shopping cart')
def step_when__item_removed_from_cart(context):
    context.cart.remove_item("item1")
    
    print("Bok removed from shopping cart")


@then(u'the user can see that the shopping cart is empty')
def step_then__verify_cart_is_empty(context):
    assert context.cart.is_empty() is True, "Shopping cart is NOT empty"


@when(u'user add items and their prices')
def step_when__items_added_to_cart(context):
    context.items = []
    context.sum_of_prices = 0

    for row in context.table:
        item = row["item"]
        price = int(row["price"])
        
        context.cart.add_item(item, price)
        
        context.items.append(item)
        context.sum_of_prices += price
        
    #context.unique_items = set(context.items)

    print("items added to shopping cart")


@then(u'the user can see the number of items and the total amount to pay for the items in the shopping cart')
def step_then__verify_nr_items_and_amount(context):
    assert (context.cart.nr_of_items() == len(context.items)), "items in shopping cart is NOT the right number"
    assert (context.cart.amount() == context.sum_of_prices), "Total amount in shopping cart is NOT the right amount"


@then(u'the user can see the count of each item in the shopping cart')
def step_then__verify_count_of_each_item(context):
    
    unique_items = {}
    
    for item in context.items:
        
        item_count = unique_items.get(item, 0)
        
        if item_count == 0:
            unique_items[item] = 1
            
        elif item_count > 0:
            unique_items[item] = item_count +1
            
    for item in context.cart.list_item():
        assert (unique_items[item["name"]] == item["count"]), "Number of unique bokks are NOT correct in the shopping cart"


@when(u'chooses to delete them all at once')
def step_when__all_items_get_removed(context):
    context.cart.delete_items()
    context.empty_cart = context.cart.is_empty()


"""

