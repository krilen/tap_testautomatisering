from behave import given, when, then

from cart import Cart

@given(u'that a shopping cart is present')
def step_give__cart_present(context):
    context.cart = Cart()
    
    print("User has access to a shopping cart")


@when(u'the user places the book in the shopping cart')
def step_when__book_added_to_cart(context):
    context.cart.add_book("Book1", 200)
    context.empty_cart = context.cart.is_empty()
    
    print("Book added to shopping cart")


@then(u'the user can see that the shopping cart is not empty')
def step_then__verify_cart_not_empty(context):
    assert context.empty_cart is False, "Shopping cart is empty"


@when(u'the user removes the book from the shopping cart')
def step_when__book_removed_from_cart(context):
    context.cart.remove_book("Book1")
    context.empty_cart = context.cart.is_empty()
    
    print("Bok removed from shopping cart")


@then(u'the user can see that the shopping cart is empty')
def step_then__verify_cart_is_empty(context):
    assert context.empty_cart is True, "Shopping cart is NOT empty"


@when(u'user add {book} and its {price:d}')
def step_when__books_added_to_cart(context, book, price):
    context.cart.add_book(book, price)

    print("Books added to shopping cart")


@then(u'the user can see the number of books and the total amount to pay for the books in the shopping cart')
def step_then__verify_nr_books_and_amount(context):
    context.amount = context.cart.amount()
    context.nr_books = context.cart.nr_of_books()
    
    assert (context.nr_books == 3), "Books in shopping cart is NOT the right number"
    assert (context.amount == 270), "Total amount in shopping cart is NOT the right amount"


@then(u'the user can see the count of each book in the shopping cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user can see the count of each book in the shopping cart')


@when(u'chooses to delete them all at once')
def step_impl(context):
    raise NotImplementedError(u'STEP: When chooses to delete them all at once')



