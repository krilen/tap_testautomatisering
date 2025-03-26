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
            | item |
            | 124  |
            | 125  |
            | 136  |
        Then the user can see the number of items and the total amount to pay for the items in the shopping cart


    Scenario: The user adds a item that already exists in the shopping cart the count of that item should increase
        Given that a shopping cart is present
        When user add items to the shopping cart
            | item |
            | 124  |
            | 125  |
            | 124  |
        Then the user can see the count of each item in the shopping cart


    Scenario: The user chooses to remove all of the items in the shopping cart
        Given that a shopping cart is present
        When user add items to the shopping cart
            | item |
            | 124  |
            | 125  |
            | 136  |
        And chooses to delete them all at once
        Then the user can see that the shopping cart is empty

