from inventory import Inventory

class Cart():
    def __init__(self):
        """
        Setup of the shopping cart
        """
        # {"cart":[{"product_id": ?, "product_name": "?", "count": ?, "price": ?, "total_price": ?}], "product_count": ?, "total_count": ?, "amount": ?, "discount": ?}
        self.shopping_cart = []

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
    def amount_discount(self):
        """
        The discount for buying more than 3 items
        """
        if self.nr_of_items > 3:
            return round((self.amount_for_items *0.1), 2)

        else:
            return 0


    @property
    def delete_all_items(self):
        """
        Delete all items in the shopping cart
        """
        self.shopping_cart.clear()


    @property
    def check_item_inventory(self):
        """
        Method that verifies the count from the inventory and the count 
        that the user want to buy.
        If needed adjusts the shopping cart to reflect the actual count in the inventory
        and informs the use about the readjustment
        """
        for item in self.list_items():

            print(item)



    def add_item(self, item_id, count=1):
        """
        Add an item and its price to the shopping cart
        """
        if count > 0:
            inventory = Inventory()
            item = inventory.product(item_id)

            for cart in self.shopping_cart:
                if cart["product_id"] == item_id:
                    cart["count"] += count
                    break

            else:
                if item:
                    self.shopping_cart.append({"product_id": item_id, "price": item[0]["price"], "count": count})


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

    c = Cart()
    c.add_item(124)
    c.add_item(124, 10)
    c.add_item(124)

    print(c.is_empty)

    c.check_item_inventory

    print("Wrong file")