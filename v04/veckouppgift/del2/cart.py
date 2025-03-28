from products import Products

class Cart():
    """
    A class to handle a shopping cart.
    it has to main methods
     * 'add_item': Adds an item to the cart
     * 'remove_item': Removes an item from the cart
    To this there are a lot of getters methods that does or return things
    """
    def __init__(self):
        """
        Setup of the shopping cart
        """
        self.shopping_cart = {"items": [],
                              "count_unique": 0, 
                              "count_total": 0,
                              "amount": 0,
                              "discount": 0
                              }
        # {"items:[{"product_id": ?, "price": ?, "count": ?, "total_price": ?}, ...], "count_unique": ..."}
        

    @property
    def is_empty(self):
        """
        Check to see if the shopping cart is empty
        """
        return not self.shopping_cart["items"]


    @property
    def nr_of_items(self):
        """
        Number of items in the shopping cart
        """
        return self.shopping_cart["count_total"]


    @property
    def nr_of_unique_items(self):
        """
        Number of unique items in the shopping cart
        """
        return self.shopping_cart["count_unique"]


    @property
    def amount_for_items(self):
        """
        The total amount for the items in the shopping cart
        """
        return round(self.shopping_cart["amount"], 2)


    @property
    def amount_discount(self):
        """
        The discount for buying more than 3 items
        """
        return round(self.shopping_cart["discount"], 2)


    @property
    def delete_all_items(self):
        """
        Delete all items in the shopping cart
        """
        self.shopping_cart["items"].clear()
        self.recalculate_cart


    @property
    def list_items(self):
        """
        List all items in the shopping cart
        """
        return self.shopping_cart["items"]


    @property
    def list_cart(self):
        """
        List the entire cart
        """
        return self.shopping_cart


    @property
    def recalculate_cart(self):
        """
        After modification of the items, values based on them needs to be recalculated
        """
        items = self.list_items
        
        self.shopping_cart["count_unique"] = len(items)
        self.shopping_cart["count_total"] = sum([item["count"] for item in items])
        self.shopping_cart["amount"] = sum([round((item["count"] *item["price"]), 2) for item in items])
        
        if self.nr_of_items > 3:
            self.shopping_cart["discount"] = round((self.amount_for_items *0.1), 2)


    def nr_of_item(self, item_id):
        """
        The count (number of) a specific item in the cart
        """
        _count = [item["count"] for item in self.list_items if item["product_id"] == item_id]

        if _count:
            return _count[0]
        
        return 0 


    def add_item(self, product_id, count=1):
        """
        Add a product to the shopping cart
        """
        # Simple checks
        if not isinstance(product_id, int):
            return False, "not a valid product id"
        
        if not isinstance(count, int) or count < 1:
            return False, "not a valid count"

        # Connect to backend to query about the products
        products = Products()
        product = products.product(product_id)

        if not product:
            return False, "product not found"

        product = product[0]
        
        product_stock_enough = True

        # When the stock is less then the requested count, 
        # adjustment is made to the requested count
        if product["stock"] < count:
            product_stock_enough = False
            count = product["stock"]

        # When the stock is 0
        if count == 0:
            return False, "no product stock found"

        else:
            # Check the current cart
            for item in self.list_items:
                # Found the item in the cart, needs to update it
                if item["product_id"] == product_id:
                    # Readjust the count if my old count and new count is
                    # larger then the current stock
                    if item["count"] +count > product["stock"]:
                        count = product["stock"] -item["count"]
                        product_stock_enough = False

                    # Update the item in the cart with the new count
                    item["count"] += count
                    item["price"] = product["price"] # Update the price just in case
                    item["total_price"] = round(item["count"] * product["price"], 2) 
                    break
            
            # Add it to the cart if the item was not found
            else:
                self.shopping_cart["items"].append({"product_id": product_id, 
                                                    "price":product["price"], 
                                                    "count": count, 
                                                    "total_price": round(count * product["price"], 2)
                                                    })

        # Recalculated the cart (amount, discount, number of items and number of unique items)
        self.recalculate_cart
        
        if not product_stock_enough:
            return True, "the requested count adjusted"
        
        return True, ""


    def remove_item(self, product_id, count=0):
        """
        Remove an item in the shopping cart either
         * reduce the number of the same item
         * remove the item
        """
        # Simple checks
        if not isinstance(product_id, int):
            return False, "not a valid product id"
        
        if not isinstance(count, int):
            return False, "not a valid count"
        
        remove_item = 0

        doing_remove_item = False

        # Go through the cart to see if the item to be removed or reduced exists
        for i, cart in enumerate(self.list_items, start=1):
            
            # The request to remove the item completly
            if cart["product_id"] == product_id and (count == 0 or cart["count"] == 1 or cart["count"] <= count):
                remove_item = i
                doing_remove_item = True
            
            # The request to reduce the count of the item
            elif cart["product_id"] == product_id and cart["count"] > 1:
                cart["count"] -= count
                cart["total_price"] = round(cart["count"] * cart["price"], 2) 

                doing_remove_item = True

        if doing_remove_item:

            # Remove the item complete while NOT in a loop
            if remove_item:
                self.list_items.pop(remove_item -1)
            
             # Recalculated the cart (amount, discount, number of items and number of unique items)
            self.recalculate_cart
            return True, ""

        else:
            # Nothing was removed
            return False, "no item removed"



if __name__ == "__main__":
    print("Wrong file")