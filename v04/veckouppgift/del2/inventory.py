from api import Api

class Inventory():
    
    def __init__(self) -> None:
        self._products = []
        
        #_api = Api("https://dummyjson.com/products/category/smartphones?select=title,price,stock")
        #_data = _api()
        #del(_api)

        _data = {"products":[{"id":121,"title":"iPhone 5s","price":199.99,"stock":65},{"id":122,"title":"iPhone 6","price":299.99,"stock":99},{"id":123,"title":"iPhone 13 Pro","price":1099.99,"stock":26},{"id":124,"title":"iPhone X","price":899.99,"stock":99},{"id":125,"title":"Oppo A57","price":249.99,"stock":76},{"id":126,"title":"Oppo F19 Pro Plus","price":399.99,"stock":92},{"id":127,"title":"Oppo K1","price":299.99,"stock":61},{"id":128,"title":"Realme C35","price":149.99,"stock":81},{"id":129,"title":"Realme X","price":299.99,"stock":87},{"id":130,"title":"Realme XT","price":349.99,"stock":53},{"id":131,"title":"Samsung Galaxy S7","price":299.99,"stock":55},{"id":132,"title":"Samsung Galaxy S8","price":499.99,"stock":75},{"id":133,"title":"Samsung Galaxy S10","price":699.99,"stock":40},{"id":134,"title":"Vivo S1","price":249.99,"stock":13},{"id":135,"title":"Vivo V9","price":299.99,"stock":19},{"id":136,"title":"Vivo X21","price":499.99,"stock":0}],"total":16,"skip":0,"limit":16}

        if _data != None:
            self._products = _data["products"]


    @property
    def products(self):
        return self._products


    @property
    def products_id(self):
        return [ p["id"] for p in self.products ]


    def product(self, id):
        return [ p for p in self.products if p["id"] == id ]
    

if __name__ == "__main__":
    i = Inventory()
    
    print(i.products)
    
    print(i.products_id)
    
    print(i.product(143))
    
    print("Wrong file")