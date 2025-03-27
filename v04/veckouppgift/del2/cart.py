from products import Products

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
    def list_cart(self):
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


    def add_item(self, product_id, count=1):
        """
        Add a product to the shopping cart
        """
        if not isinstance(product_id, int):
            return False, "not a valid product id"
        
        if not isinstance(count, int):
            return False, "not a valid count"

        if count < 1:
            return False, "only positive number for products count"

        products = Products()
        product = products.product(product_id)

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
                        product_stock_enough = False

                    item["count"] = item["count"] +count
                    item["price"] = product["price"] # Update the price just in case
                    item["total_price"] = round(item["count"] * product["price"], 2) 
                    break

            else:
                self.shopping_cart["items"].append({"product_id": product_id, 
                                                    "price":product["price"], 
                                                    "count": count, 
                                                    "total_price": round(count * product["price"], 2)
                                                    })

        self.recalculate_cart
        
        if not product_stock_enough:
            return False, "the count for the cart has changed"
        
        return True, "product added to the cart"


    def remove_item(self, product_id, count=1):
        """
        Remove an item in the shopping cart either
         * reduce the number of the same item
         * remove the item
        """
        if not isinstance(product_id, int):
            return False, "not a valid product id"
        
        if not isinstance(count, int):
            return False, "not a valid count"
        
        remove_item = 0

        for i, cart in enumerate(self.list_items, start=1):
            
            if cart["product_id"] == product_id and (count == 0 or cart["count"] == 1 or cart["count"] <= count):
                remove_item = i
                
            elif cart["product_id"] == product_id and cart["count"] > 1:
                cart["count"] -= count

        if remove_item:
            self.list_items.pop(remove_item -1)
            self.recalculate_cart
            return True, "the product was removed from the cart"
            
        self.recalculate_cart
        return True, "reduced the count of the product id in the cart"


if __name__ == "__main__":
    print("Wrong file")