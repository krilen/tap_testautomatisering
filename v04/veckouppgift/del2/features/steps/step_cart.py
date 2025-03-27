from behave import given, when, then

from cart import Cart

@given(u'that a shopping cart is present')
def step_given__shopping_cart_present(context):
    context.cart = Cart()

    print("A shopping cart is present")


@when(u'the user places the item in the shopping cart')
def step_when___add_item_to_cart(context):
    context.cart.add_item(124)
    
    print("Item added to the shopping cart")    
    

@then(u'the user can see that the shopping cart is not empty')
def step_then__shopping_cart_not_empty(context):
    assert context.cart.is_empty is False, "Shopping cart is empty"


@when(u'the user removes the item from the shopping cart')
def step_when__remove_item_fom_cart(context):
    context.cart.remove_item(124)

    print("Item removed from the shopping cart")  


@then(u'the user can see that the shopping cart is empty')
def step_then_shopping_cart_is_empty(context):
    assert context.cart.is_empty is True, "Shopping cart is NOT empty"


@when(u'user add items to the shopping cart')
def step_when__add_items_to_cart(context):
    context.items = []
    context.sum_of_prices = 0.0

    for row in context.table:
        item = int(row["item_id"])
        price = float(row["price"])
        count = int(row["count"])
        
        context.cart.add_item(item, count)
        
        context.items.append({"item_id": item, "price": price, "count": count})
        context.sum_of_prices += price
        
    print("Items added to shopping cart")


@then(u'the user can see the number of items and the total amount to pay for the items in the shopping cart')
def step_then__user_can_see_number_of_items_and_total_amount(context):
    assert (context.cart.nr_of_items == len(context.items)), "Items in shopping cart is NOT the right count"
    assert (context.cart.amount_for_items == context.sum_of_prices), "Total amount in the shopping cart is NOT the right value"


@then(u'the user can see the count of each item in the shopping cart')
def step_then__verify_count_of_each_item(context):
    unique_items = {}
    
    for item in context.items:

        item_id = item["item_id"]
        item_count = item["count"]
        
        item_count_found = unique_items.get(item_id, 0)

        if item_count_found == 0:
            unique_items[item_id] = item_count
            
        elif item_count_found > 0:
            unique_items[item_id] = item_count_found +item_count
            
    for item in context.cart.list_items():
        assert (unique_items[item["product_id"]] == item["count"]), "Number of unique items are NOT correct in the shopping cart"


@when(u'chooses to delete them all at once')
def step_when__all_items_get_removed(context):
    context.cart.delete_all_items

    print("Clear the shopping cart")


# discount
@when(u'item are added to the shopping cart with a different {count:d}')
def step_when__items_added_to_cart_with_count(context, count):
    for row in context.table:
        item_id2 = int(row["item_id"])
        price2 = float(row["price"])

    context.cart.add_item(item_id2, count)
    
    context.items = []

    for _ in range(count):
        context.items.append(item_id2)

    if count > 3:
        context.sum_of_prices = price2 *count
        context.discount = round((context.sum_of_prices * 0.1), 2) # 10% discrount

    elif count > 0:
        context.sum_of_prices = price2 *count
        context.discount = 0

    else:
        context.sum_of_prices = 0
        context.discount = 0

    print("Adding items to verify the discount when adding", count, "items")


# discount
@then(u'if a discount for buying more then 3 items are provided')
def step_then__verify_if_discount_is_proviced(context):
    assert (context.cart.amount_discount == context.discount), "The discunt are NOT correct in the shopping cart"


# inventory
@then(u'if the user {count:d} exceeds the inventory account the user count readjusted to the inventory')
def step_then__verify_inventory_if_needed_reajust(context, count):
    pass


# inventory
@then(u'the user is informed if the count has been changed')
def step_then__user_infromed_by_count_change(context):
    pass