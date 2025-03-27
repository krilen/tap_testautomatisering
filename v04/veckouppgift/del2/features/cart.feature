Feature: Handle shopping cart
    As a customer I want to place my items and handle my bitemsooks using a shopping cart


    Scenario: The user should be able to add items to a shopping cart
        Given that a shopping cart is present
        When the user places the item in the shopping cart
        Then the user can see that the shopping cart is not empty


    Scenario: The user should be able to remove items from the shopping cart
        Given that a shopping cart is present
        When the user places the item in the shopping cart
        And the user removes the item from the shopping cart
        Then the user can see that the shopping cart is empty


    Scenario: The user should always be able to see the number of items in the cart and the total amount to pay
        Given that a shopping cart is present
        When user add items to the shopping cart
            | item_id | price  | count |
            | 124     | 899.99 | 1     |
            | 125     | 249.99 | 1     |
            | 136     | 499.99 | 1     |
        Then the user can see the number of items and the total amount to pay for the items in the shopping cart


    Scenario: The user adds a item that already exists in the shopping cart the count of that item should increase
        Given that a shopping cart is present
        When user add items to the shopping cart
            | item_id | price  | count |
            | 124     | 899.99 | 2     |
            | 125     | 249.99 | 1     |
            | 125     | 249.99 | 1     |
        Then the user can see the count of each item in the shopping cart


    Scenario: The user chooses to remove all of the items in the shopping cart
        Given that a shopping cart is present
        When user add items to the shopping cart
            | item_id | price  | count |
            | 124     | 899.99 | 1     |
            | 125     | 249.99 | 1     |
            | 136     | 499.99 | 1     |
        And chooses to delete them all at once
        Then the user can see that the shopping cart is empty


    Scenario Outline: If the user buys more than 3 items a discount of 10% on the whole amount should be added
        Given that a shopping cart is present
        When item are added to the shopping cart with a different <count>
            | item_id | price  |
            | 125     | 249.99 |
        Then the user can see the number of items and the total amount to pay for the items in the shopping cart
        And if a discount for buying more then 3 items are provided

        Examples:
            | count |
            | 3     |
            | 4     |
            | -1000 |
            | 64000 |


    Scenario Outline: The user buys items and the number of items availblefor purchase is verified against the inventory
        Given that a shopping cart is present        
        When item are added to the shopping cart with a different <count>
            | item_id | price  |
            | 125     | 249.99 |
        Then if the user <count> exceeds the inventory account the user count readjusted to the inventory
        And the user is informed if the count has been changed
        And the user can see the number of items and the total amount to pay for the items in the shopping cart

        Examples:
            | count | inform |
            | 1     | 0      |
            | 76    | 0      |
            | 77    | 1      |
            | -10   | 0      |