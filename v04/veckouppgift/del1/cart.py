


class Cart():
    def __init__(self):
        self.cart = []


    def is_empty(self):
        return not self.cart
    

    def add_book(self, book, price):   
        for item in self.cart:
            
            if item['name'] == book:
                item["count"] += 1
                break

        else:
            self.cart.append({"name": book, "price": price, "count": 1})


    def list_book(self):
        return self.cart


    def remove_book(self, book):
        remove_item = 0

        for i, item in enumerate(self.cart, start=1):

            if item["name"] == book and item["count"] > 1:
                item["count"] -= 1

            elif item["name"] == book and item["count"] == 1:
                remove_item = i

        if remove_item:
            self.cart.pop(remove_item -1)


    def nr_of_books(self):
        return sum([item["count"] for item in self.cart])

    
    def nr_of_unique_books(self):
        return len(self.cart)


    def amount(self):
        return sum([item["count"] * item["price"] for item in self.cart])


    def delete_books(self):
        self.cart.clear()

"""
if __name__ == "__main__":
    cart = Cart()

    print(f"Is cart empty: {cart.is_empty()}")
    print(f"Number of books: {cart.nr_of_books()}")
    print(f"Number of unique books: {cart.nr_of_unique_books()}")
    print(f"Total amount: {cart.amount()}")

    print("Add a book")
    cart.add_book("Book1", 100)

    print(f"Is cart empty: {cart.is_empty()}")
    print(f"Number of books: {cart.nr_of_books()}")
    print(f"Number of unique books: {cart.nr_of_unique_books()}")
    print(f"Total amount: {cart.amount()}")

    print("Add another book")
    cart.add_book("Book2", 200)

    print("Add the same book again")
    cart.add_book("Book2", 200)
    print(f"Number of books: {cart.nr_of_books()}")
    print(f"Number of unique books: {cart.nr_of_unique_books()}")
    print(f"Total amount: {cart.amount()}")

    cart.remove_book("Book1")
    print("remove book1")
    cart.remove_book("Book2")
    print("remove book2")

    print(f"Is cart empty: {cart.is_empty()}")
    print(f"Number of books: {cart.nr_of_books()}")
    print(f"Number of unique books: {cart.nr_of_unique_books()}")
    print(f"Total amount: {cart.amount()}")

    cart.remove_book("Book2")
    print("remove book2")
    print(f"Is cart empty: {cart.is_empty()}")
    print(f"Number of books: {cart.nr_of_books()}")
    print(f"Number of unique books: {cart.nr_of_unique_books()}")
    print(f"Total amount: {cart.amount()}")
"""