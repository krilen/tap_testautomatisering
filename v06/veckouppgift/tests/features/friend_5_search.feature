Feature: Search friends

# US12  
# som en användare  
# vill jag kunna söka upp en vän  
# så att snabbt får fram vännens uppgifter


    Scenario: Search after friends
        Given access to the list webpage
        Then I can remove them all 
        When I add a friend
        And a second friend
        Then I can search after them
            | search | count |
            | john   | 1     |
            | mike   | 0     |
            | spam   | 2     |
            | mary   | 1     |
            | doe    | 2     |
            | net    | 1     |
            | com    | 1     |
            | org    | 0     |
            | 0      | 0     |
