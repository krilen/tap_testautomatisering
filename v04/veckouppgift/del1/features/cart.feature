Feature: Handle shopping cart
    As a customer I want to place my books and handle my books using a shopping cart

    Scenario: The user should be able to add books to a shopping cart
        Given that a shopping cart is present
        When the user places the book in the shopping cart
        Then the user can see that the shopping cart is not empty


    Scenario: The user should be able to remove books from the shopping cart
        Given that a shopping cart is present
        When the user places the book in the shopping cart
        And the user removes the book from the shopping cart
        Then the user can see that the shopping cart is empty

    Scenario: The user should always be able to see the number of books in the cart and the total amount to pay
        Given that a shopping cart is present
        When user add books and their prices
            | book  | price |
            | book1 | 100   |
            | book2 | 150   |
            | book3 | 120   |
        Then the user can see the number of books and the total amount to pay for the books in the shopping cart

    Scenario: The user adds a book that already exists in the shopping cart the count of that book should increase
        Given that a shopping cart is present
        When user add books and their prices
            | book  | price |
            | book1 | 100   |
            | book2 | 150   |
            | book1 | 100   |
        Then the user can see the count of each book in the shopping cart

    Scenario: The user chooses to remove all of the books in the shopping cart
        Given that a shopping cart is present
        When user add books and their prices
            | book  | price |
            | book1 | 100   |
            | book2 | 150   |
            | book3 | 120   |
        And chooses to delete them all at once
        Then the user can see that the shopping cart is empty

