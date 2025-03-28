from behave import given, when, then

from cart import Cart
from products import Products
from user import User


@given(u'that a shopping cart is present')
def step_given__shopping_cart_present(context):
    context.cart = Cart()
    context.products = Products()

    print("A shopping cart is present")


@given(u'the user can see that the shopping cart is empty')
def step_given__shopping_cart_is_empty(context):
    assert context.cart.is_empty is True, "Shopping cart is NOT empty"


@when(u'the user places the item in the shopping cart')
def step_when__add_item_to_cart(context):
    context.cart.add_item(124)
    
    print("Item added to the shopping cart")    


@then(u'the user can see that the shopping cart is not empty')
def step_then__cart_not_empty(context):
    assert context.cart.is_empty is False, "Shopping cart is empty"


@when(u'the user removes the item from the shopping cart')
def step_when__remove_item_fom_cart(context):
    context.cart.remove_item(124, 1) # Removes a single item

    print("Item removed from the shopping cart")  


@then(u'the user can see that the shopping cart is empty')
def step_then__cart_is_empty(context):
    assert context.cart.is_empty is True, "Shopping cart is NOT empty"


@then(u'the user removes all of the items from the shopping cart')
def step_then__cart_is_cleared(context):
    context.cart.delete_all_items # Clears the cart

    print("The shopping cart is cleared (all items removed)")  


@when(u'user adds items: {items_str} of different count of:{count_str} to the shopping cart')
def step_when__items_added_with_count_to_cart(context, items_str, count_str):
    context.items = {}
    context.sum_price = 0
    
    items = [int(x) for x in items_str.split(",")]
    _count = [int(x) for x in count_str.split(",")]

    for i, item in enumerate(items):
        count = _count[i]

        # Add item to the cart using the requested count
        add, err = context.cart.add_item(item, count)

        # An add of items was sucessful
        if add:       
            # If add to the cart was done butwith  a message about the requested count
            if err == "the requested count adjusted":
                # Since we requested an item with a to high account lets take the maximum count
                # but we also must be aware of what we already have in the cart or context verification cart
                context_count = 0

                if context.items.get(item, False):
                    context_count = sum([x[1] for x in context.items[item]])

                count = context.products.product(item)[0]["stock"] -context_count

            # Add data for verification
            _stock = context.products.product(item)[0]["stock"]
            _price = context.products.product(item)[0]["price"]

            _data = (_count[i], count, err, _price, _stock)
        
            # _data index
            # 0: the requested count of item
            # 1: the actual count of item
            # 2: error message when adding
            # 3: price of the item
            # 4: actual inventory stock

            if context.items.get(item, {}):
                context.items[item].append(_data)
            else:
                context.items[item] = [_data]
            
            # Total amount of the items, 
            # REMEMBER THE ISSUE WITH PYTHON AND FLOATS
            context.sum_price += round(count * _price, 2)

            print("Added", item, "(requested count:", _count[i], ") added count:", count, "and price:", _price )

    print("Done adding items to the cart")


@then(u'the user can see the total number of items and the total amount to pay for the items in the shopping cart')
def step_then__user_can_see_total_number_of_items_and_total_amount(context):
    
    # Verify the total amount to pay (disregrad any discount)
    assert(round(context.sum_price, 2) == context.cart.amount_for_items), "Total amount in the shopping cart is NOT the right value"
    
    # Verify yhe number of items (all)
    nr_of_items_actual_count = 0
    nr_of_items_requested_count = 0

    for item in context.items:
        for each_item in context.items[item]:
            nr_of_items_actual_count += each_item[1]
            nr_of_items_requested_count += each_item[0]

    if nr_of_items_actual_count != nr_of_items_requested_count:
        assert(nr_of_items_actual_count == context.cart.nr_of_items), "Total number of the actual count of items is NOT correct"
    else:
        assert(nr_of_items_requested_count == context.cart.nr_of_items), "Total number of the requested count of items is NOT correct"


@then(u'the user can see the count of each item in the shopping cart')
def step_then__verify_total_count_of_each_item(context):

    # Verify the total amout for each item
    for item in context.items:
        nr_of_total_count = 0

        for each_item in context.items[item]:
            nr_of_total_count += each_item[1]

        assert(nr_of_total_count == context.cart.nr_of_item(item)), "Total total number count for the specific item is NOT correct"



# discount
@then(u'if a discount for buying more then 3 items are provided')
def step_then__verify_if_discount_is_provided(context):
    nr_of_item = 0
    amount = 0

    for item in context.items:
        for each_item in context.items[item]:

            nr_of_item += each_item[1]
            amount += round(each_item[1] * each_item[3], 2)


    if nr_of_item > 3:
        assert (context.cart.amount_discount == round(amount *0.1, 2)), "The correct discount was NOT provided and that is NOT correct"

    else:
        assert (context.cart.amount_discount == 0), "The discount was provided and that is NOT correct"        


# inventory
@then(u'the user is informed if the count has been changed')
def step_then__user_infromed_by_count_change(context):

    for item in context.items:
        items_count_in_cart = 0

        for each_item in context.items[item]:
            items_count_in_cart += each_item[1]

            # The adding to the cart was NOT successful
            if each_item[0] != each_item[1] and items_count_in_cart == each_item[4]:
                assert (len(each_item[2]) > 0), "The message about the inventory was empty"  

            # Adding to the cart was successful
            else:
                assert (len(each_item[2]) == 0), "The message about the inventory was NOT empty"  
        

# login
@when(u'the user submits login credentials ({username:w} and {password:w}) and presse the logn button')
def step_when__submitting_login_credentials(context, user, password):
    pass

# login
@then(u'a message will inform about the status of the login')
def step_then__login_message_informs_the_user(context):
    pass

