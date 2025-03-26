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
    
    print("Bok removed from shopping cart")


@then(u'the user can see that the shopping cart is empty')
def step_then__verify_cart_is_empty(context):
    assert context.cart.is_empty() is True, "Shopping cart is NOT empty"


@when(u'user add books and their prices')
def step_when__books_added_to_cart(context):
    context.books = []
    context.sum_of_prices = 0

    for row in context.table:
        book = row["book"]
        price = int(row["price"])
        
        context.cart.add_book(book, price)
        
        context.books.append(book)
        context.sum_of_prices += price
        
    #context.unique_books = set(context.books)

    print("Books added to shopping cart")


@then(u'the user can see the number of books and the total amount to pay for the books in the shopping cart')
def step_then__verify_nr_books_and_amount(context):
    assert (context.cart.nr_of_books() == len(context.books)), "Books in shopping cart is NOT the right number"
    assert (context.cart.amount() == context.sum_of_prices), "Total amount in shopping cart is NOT the right amount"


@then(u'the user can see the count of each book in the shopping cart')
def step_then__verify_count_of_each_book(context):
    
    unique_books = {}
    
    for book in context.books:
        
        book_count = unique_books.get(book, 0)
        
        if book_count == 0:
            unique_books[book] = 1
            
        elif book_count > 0:
            unique_books[book] = book_count +1
            
    for item in context.cart.list_book():
        assert (unique_books[item["name"]] == item["count"]), "Number of unique bokks are NOT correct in the shopping cart"


@when(u'chooses to delete them all at once')
def step_when__all_books_get_removed(context):
    context.cart.delete_books()
    context.empty_cart = context.cart.is_empty()




