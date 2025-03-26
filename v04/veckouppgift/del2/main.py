from cart import Cart
from inventory import Inventory


def view_items(inventory, cart):
    
    while True:
        
        print()
        print(" Items that can be bought")
        
        for i, product in enumerate(inventory.products, start=1):
            print(f"  - {i}. {product["title"]} (${product["price"]})")
                

        print()
        print(" > Press 'e' to go back to the main menu")
        print(" > Press the corresponding number of the item to put it into you cart")
        print()
        command = input(" Your selection >> ").casefold()[:1]

        match command:
            case "e":
                break

            case _:
                print(" Not a valid option")


def view_cart(cart):
    
    while True:
        
        print()
        print(" Items that is in your shopping cart")
        
        for i, item in enumerate(cart.list_items(), start=1):
            print(f"  - {i}. {item["product_id"]} {item["price"]} {item["count"]}")
            
        else:
            print("  - No items found")
            
        print()
        print(" > Press 'e' to go back to the main menu")
        print(" > Press the corresponding number of the item in your cart to modify")
        print()
        command = input(" Your selection >> ").casefold()[:1]

        match command:
            case "e":
                break

            case _:
                print(" Not a valid option")

def main():
    
    inventory = Inventory()
    cart = Cart()
    
    while True:
    
        print(" Welcome to the TERMINAL shop!")
        print()
        print(" > Press 'q' to quit")
        print(" > Press 'c' to see your shopping cart")
        print(" > Press 'i' to see the items that can be bought")
        print()
        command = input(" Your selection >> ").casefold()[:1]
        
        match command:
            case "i":
                view_items(inventory, cart)
                
            case "c":
                view_cart(cart)
            
            case "q":
                print()
                print(" Thank you for visiting the TERMINAL shop!")
                print(" Have a nice day")
                break

            case _:
                print(" Not the valid option")

if __name__ == "__main__":
    main()