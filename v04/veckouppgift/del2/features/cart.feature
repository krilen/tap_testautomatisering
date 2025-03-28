Feature: Handle shopping cart
    As a user I want to place items and handle the items using a shopping cart


    # Adds an item to the cart and verifies that that cart is not empty

    Scenario: The user should be able to add items to a shopping cart
        Given that a shopping cart is present
        And the user can see that the shopping cart is empty
        When the user places the item in the shopping cart
        Then the user can see that the shopping cart is not empty


    # Adds an item to the cart and removes the item 
    # to verify that tha cart is now empty
    
    Scenario: The user should be able to remove items from the shopping cart
        Given that a shopping cart is present
        When the user places the item in the shopping cart
        And the user removes the item from the shopping cart
        Then the user can see that the shopping cart is empty


    # Adds 3 items (same product) to the cart and removes 1 item
    # verifies that the cart is not empty and clears the cart
    # then verifies that the cart is now empty

    Scenario: The user should be able to remove a single item and then the rest of the items from the shopping cart
        Given that a shopping cart is present
        When the user places the item in the shopping cart
        And the user places the item in the shopping cart
        And the user places the item in the shopping cart
        And the user removes the item from the shopping cart
        Then the user can see that the shopping cart is not empty
        And the user removes all of the items from the shopping cart
        Then the user can see that the shopping cart is empty


    # Adds different count of items (also 0 or negative amounts)
    # Verifies the number of total items and the correct amount to pay

    Scenario Outline: The user should always be able to see the number of items in the cart and the total amount to pay
        Given that a shopping cart is present
        When user adds items: <items> of different count of: <count> to the shopping cart
        Then the user can see the total number of items and the total amount to pay for the items in the shopping cart

        Examples:
            | items       | count    |
            | 124         | 12       |
            | 124,125,135 | 10,10,10 |
            | 124         | -10      |
            | 124,125     | 10,0     |
            | 2000        | 10       |


    # Adding the same item several times with count
    # Verifies that the number count for the item increase

    Scenario Outline: The user adds an item that already exists in the shopping cart the count of that item should increase
        Given that a shopping cart is present
        When user adds items: <items> of different count of: <count> to the shopping cart
        Then the user can see the count of each item in the shopping cart

        Examples:
            | items       | count    |
            | 124         | 12       |
            | 124,124     | 10,-10   |
            | 124,125,124 | 10,10,10 |
            | 124,124     | 0,10     |
            | 200,200     | 100,1    |
            | 124,124     | 1000,1   |


    # Adding items to the cart and verify that all can be removed at once

    Scenario Outline: The user chooses to remove all of the items in the shopping cart
        Given that a shopping cart is present
        When user adds items: <items> of different count of: <count> to the shopping cart
        Then the user removes all of the items from the shopping cart
        Then the user can see that the shopping cart is empty

        Examples:
            | items       | count    |
            | 124         | 0        |
            | 124,124     | 10,-10   |
            | 124,125     | 10,40,10 |
            | 124,124     | 2000,1   |

    # Verifying when the user adds more than 3 items a discount of 10%

    Scenario Outline: If the user buys more than 3 items a discount of 10% on the whole amount should be added
        Given that a shopping cart is present
        When user adds items: <items> of different count of: <count> to the shopping cart
        Then the user can see the total number of items and the total amount to pay for the items in the shopping cart
        And if a discount for buying more then 3 items are provided

        Examples:
            | items       | count    |
            | 124         | 0        |
            | 124         | 3        |
            | 124         | -100     |
            | 124         | 6500     |
            | 124,125     | 3,1      |


    # Verifying when the user adds more than the inventory has the actual count is only added to the cart

    Scenario Outline: The user buys items and the request number (count) is verified against the inventory and modified if needed and inform the user
        Given that a shopping cart is present        
        When user adds items: <items> of different count of: <count> to the shopping cart
        Then the user can see the total number of items and the total amount to pay for the items in the shopping cart
        And the user is informed if the count has been changed

        Examples:
            | items                   | count              |
            | 124                     | 0                  |
            | 124                     | -3                 |
            | 124                     | 6500               |
            | 124,124                 | 50,100             |
            | 124,124                 | 100,100            |
            | 124,125                 | 50,100             |
            | 125,125,124,125,123,125 | 10,20,100,30,26,20 |
 

    # Verify that the user must login with vaild credentials before a order can be done
    Scenario Outline: The user buys items and the request number (count) is verified against the inventory and modified if needed and inform the user
        Given that a shopping cart is present       
        When the user places the item in the shopping cart
        Then the user can see that the shopping cart is not empty
        When the user submits login credentials ("<username>" and "<password>") and presses the login button
        Then a message will inform about the status of the login

        Examples:
            | username    | password   | 
            | john        |            | 
            |             | mypass     | 
            |             |            | 
            | mary        | 12345      | 
            | john        | mypass     |