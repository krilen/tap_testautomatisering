from inventory import Inventory

class Cart():
    def __init__(self):
        """
        Setup of the shopping cart
        """
        self.shopping_cart = []
        self.inventory = Inventory()

    @property
    def is_empty(self):
        """
        Check to see if the shopping cart is empty
        """
        return not self.shopping_cart


    @property
    def nr_of_items(self):
        """
        Number of items in the shopping cart
        """
        return sum([item["count"] for item in self.shopping_cart])


    @property
    def nr_of_unique_items(self):
        """
        Number of unique items in the shopping cart
        """
        return len(self.shopping_cart)


    @property
    def amount_for_items(self):
        """
        The total amount for the items in the shopping cart
        """
        return sum([item["count"] * item["price"] for item in self.shopping_cart])


    @property
    def delete_all_items(self):
        """
        Delete all items in the shopping cart
        """
        self.shopping_cart.clear()


    def add_item(self, item_id, price):
        """
        Add an item and its price to the shopping cart
        """
        for cart in self.shopping_cart:
            
            if cart["product_id"] == item_id:
                cart["count"] += 1
                break

        else:
            self.shopping_cart.append({"product_id": item_id, "price": price, "count": 1})


    def list_items(self):
        """
        List all items in the shopping cart
        """
        return self.shopping_cart


    def remove_item(self, item_id):
        """
        Remove an item in the shopping cart either
         * reduce the number of the same item
         * remove the item
        """
        remove_item = 0

        for i, cart in enumerate(self.shopping_cart, start=1):

            if cart["product_id"] == item_id and cart["count"] > 1:
                cart["count"] -= 1

            elif cart["product_id"] == item_id and cart["count"] == 1:
                remove_item = i

        if remove_item:
            self.shopping_cart.pop(remove_item -1)


if __name__ == "__main__":
    print("Wrong file")