from inventory import Inventory

class Cart():
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
        
        # {"items:[{"product_id": ?, "price": ?, "count": ?, "total_price": ?}, ...], ..."}

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
        return self.shopping_cart["amount"]


    @property
    def amount_discount(self):
        """
        The discount for buying more than 3 items
        """
        return self.shopping_cart["discount"]


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
    def recalculate_cart(self):
        pass


    def add_item(self, product_id, count=1):
        """
        Add a product to the shopping cart
        """
        if not isinstance(product_id, int):
            return False, "not a valid product id"

        if count < 1:
            return False, "only positive number of products can be ordered"

        inventory = Inventory()
        product = inventory.product(product_id)

        print(product)

        if not product:
            return False, "product not found"
        
        product = product[0]
        
        product_stock_enough = True

        if product["stock"] < count:
            product_stock_enough = False
            count = product["stock"]

        if count == 0:
            return False, "no product stock found"

        else:

            for item in self.list_items:
                if item["product_id"] == product_id:
                    if item["count"] +count > product["stock"]:
                        count = product["stock"] -item["count"]

                    item["count"] = count
                    item["price"] = product["price"]                        # Update the price just in case
                    item["total_price"] = item["count"] * product["price"] 
                    break

            else:
                self.shopping_cart["items"].append({"product_id": product_id, 
                                                    "price":product["price"], 
                                                    "count": count, 
                                                    "total_price": count * product["price"]
                                                    })

        if not product_stock_enough:
            return product_stock_enough, "the count for the cart has changed"
        
        return True, "product added to the cart"


        




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
    print(c.is_empty)

    resp = c.add_item(124)

    print(resp)

    # HERE I AM

    print(c.is_empty)

    #print("Wrong file")